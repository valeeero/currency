from decimal import Decimal

from bs4 import BeautifulSoup

from celery import shared_task

from currency.models import Rate

from django.conf import settings
from django.core.mail import send_mail

import requests


def round_currency(num):
    return Decimal(num).quantize(Decimal('.01'))


def currency_codes(args):
    currency_type = ()
    if args == 840:
        currency_type = 'USD'
    elif args == 978:
        currency_type = 'EUR'
    return currency_type


# @shared_task
# def debug_tasks(sleep_time: int = 5):
#     from currency.models import Rate
#     print(f'Count Rates: {Rate.objects.count()}')


@shared_task
def contact_us(subject, full_email_body):
    send_mail(
        subject,
        full_email_body,
        settings.EMAIL_HOST_USER,
        [settings.SUPPORT_EMAIL],
        fail_silently=False,
    )


@shared_task
def parce_privatbank():

    privatbank_currency_url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(privatbank_currency_url)

    response.raise_for_status()

    rates = response.json()
    source = 'PrivatBank'
    available_currency_types = ('USD', 'EUR')

    for rate in rates:
        currency_type = rate['ccy']
        if currency_type in available_currency_types:
            sale = round_currency(rate['sale'])
            buy = round_currency(rate['buy'])

            last_rate = Rate.objects.filter(
                type=currency_type,
                source=source,
            ).order_by('created').last()

            if (
                    last_rate is None or
                    last_rate.sale != sale or
                    last_rate.buy != buy
            ):
                Rate.objects.create(
                    type=currency_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )


@shared_task
def parce_monobank():

    mono_currency_url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(mono_currency_url)

    response.raise_for_status()

    rates = response.json()
    source = 'MonoBank'
    available_currency_types = (840, 978)   # 840 - USD, 978 - EUR

    for rate in rates:
        currency_type_number = rate['currencyCodeA']

        currency_type_UAH = rate['currencyCodeB']

        if currency_type_UAH == 980:    # 980 - UAH

            if currency_type_number in available_currency_types:
                sale = round_currency(rate['rateSell'])
                buy = round_currency(rate['rateBuy'])

                last_rate = Rate.objects.filter(
                    type=currency_codes(currency_type_number),
                    source=source,
                ).order_by('created').last()

                if (
                        last_rate is None or
                        last_rate.sale != sale or
                        last_rate.buy != buy
                ):
                    Rate.objects.create(
                        type=currency_codes(currency_type_number),
                        sale=sale,
                        buy=buy,
                        source=source,
                    )
        else:
            continue


@shared_task
def parce_vkurse():

    vkurse_currency_url = 'http://vkurse.dp.ua/course.json'
    response = requests.get(vkurse_currency_url)

    response.raise_for_status()

    rates = response.json()
    source = 'Vkurse'

    for rate in rates:
        type_currency = ()
        sale = rates[rate]['sale']
        buy = rates[rate]['buy']

        if rate == 'Dollar':
            type_currency = 'USD'
        elif rate == 'Euro':
            type_currency = 'EUR'
        elif rate == 'Rub':
            type_currency = 'RUB'

        last_rate = Rate.objects.filter(
            type=type_currency,
            source=source,
        ).order_by('created').last()

        if (
                last_rate is None or
                last_rate.sale != round_currency(sale) or
                last_rate.buy != round_currency(buy)
        ):

            Rate.objects.create(
                type=type_currency,
                sale=sale,
                buy=buy,
                source=source,
            )


@shared_task
def parce_alfa():

    currency_url = 'https://alfabank.ua/ru'
    source = 'AlfaBank'
    response = requests.get(currency_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    type_currency_usd = soup.find_all('div', {'class': 'title'})[0].text.strip()
    type_currency_eur = soup.find_all('div', {'class': 'title'})[1].text.strip()

    eur_buy = soup.find('span', {'data-currency': 'EUR_BUY'}).text.strip()
    eur_sale = soup.find('span', {'data-currency': 'EUR_SALE'}).text.strip()
    usd_buy = soup.find('span', {'data-currency': 'USD_BUY'}).text.strip()
    usd_sale = soup.find('span', {'data-currency': 'USD_SALE'}).text.strip()

    # =========USD========
    last_rate = Rate.objects.filter(
        type=type_currency_usd,
        source=source,
    ).order_by('created').last()

    if (
            last_rate is None or
            last_rate.sale != round_currency(usd_sale) or
            last_rate.buy != round_currency(usd_buy)
    ):

        Rate.objects.create(
            type=type_currency_usd,
            sale=usd_sale,
            buy=usd_buy,
            source=source,
        )
    # =========EUR========
    last_rate = Rate.objects.filter(
        type=type_currency_eur,
        source=source,
    ).order_by('created').last()

    if (
            last_rate is None or
            last_rate.sale != round_currency(eur_sale) or
            last_rate.buy != round_currency(eur_buy)
    ):
        Rate.objects.create(
            type=type_currency_eur,
            sale=eur_sale,
            buy=eur_buy,
            source=source,
        )


@shared_task
def parce_oshad():

    currency_url = 'https://www.oschadbank.ua/currency-rate'
    source = 'OshadBank'
    response = requests.get(currency_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    type_currency_usd = soup.find_all("span", {
        "class": "heading-block-currency-rate__table-txt body-regular"
    })[7].get_text()

    usd_buy = round_currency(soup.find_all("span", {
        "class": "heading-block-currency-rate__table-txt body-regular"
    })[9].get_text())

    usd_sale = round_currency(soup.find_all("span", {
        "class": "heading-block-currency-rate__table-txt body-regular"
    })[10].get_text())

    last_rate = Rate.objects.filter(
        type=type_currency_usd,
        source=source,
    ).order_by('created').last()

    if (
            last_rate is None or
            last_rate.sale != usd_sale or
            last_rate.buy != usd_buy
    ):
        Rate.objects.create(
            type=type_currency_usd,
            sale=usd_sale,
            buy=usd_buy,
            source=source,
        )

    type_currency_eur = soup.find_all("span", {
        "class": "heading-block-currency-rate__table-txt body-regular"
    })[13].get_text()
    eur_buy = round_currency(soup.find_all("span", {
        "class": "heading-block-currency-rate__table-txt body-regular"
    })[15].get_text())
    eur_sale = round_currency(soup.find_all("span", {
        "class": "heading-block-currency-rate__table-txt body-regular"
    })[16].get_text())

    last_rate = Rate.objects.filter(
        type=type_currency_eur,
        source=source,
    ).order_by('created').last()

    if (
            last_rate is None or
            last_rate.sale != eur_sale or
            last_rate.buy != eur_buy
    ):
        Rate.objects.create(
            type=type_currency_eur,
            sale=eur_sale,
            buy=eur_buy,
            source=source,
        )


@shared_task
def parce_ukrgasbank():

    currency_url = 'https://www.ukrgasbank.com/kurs/'
    source = 'UkrGasBank'

    response = requests.get(currency_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    usd_buy = round_currency(soup.find_all("td", {"class": "val"})[0].text)/100
    usd_sale = round_currency(soup.find_all("td", {"class": "val"})[1].text)/100
    eur_buy = round_currency(soup.find_all("td", {"class": "val"})[3].text)/100
    eur_sale = round_currency(soup.find_all("td", {"class": "val"})[4].text)/100

    last_rate = Rate.objects.filter(
        type='USD',
        source=source,
    ).order_by('created').last()

    if (
            last_rate is None or
            last_rate.sale != usd_sale or
            last_rate.buy != usd_buy
    ):
        Rate.objects.create(
            type='USD',
            sale=usd_sale,
            buy=usd_buy,
            source=source,
        )

    last_rate = Rate.objects.filter(
        type='EUR',
        source=source,
    ).order_by('created').last()

    if (
            last_rate is None or
            last_rate.sale != eur_sale or
            last_rate.buy != eur_buy
    ):
        Rate.objects.create(
            type='EUR',
            sale=eur_sale,
            buy=eur_buy,
            source=source,
        )
