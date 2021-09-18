from django import forms

from currency.models import Rate, Source # noqa


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'buy',
            'sale',
            'source',
            'type',
        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'source_url',
            'name',
        )
#
# last_rate = Rate.objects.filter(
#                 type=currency_type,
#                 source=source,
#             ).order_by('created').last()
#
#             if last_rate.sale != sale or last_rate.buy != buy:
#                 Rate.objects.create(
#                     type=currency_type,
#                     sale=sale,
#                     buy=buy,
#                     source=source,
#                 )
#
# def round_currency(num):
#     return Decimal(num).quantize(Decimal('.01'))
