from django.shortcuts import render, get_object_or_404  # noqa
from currency.models import ContactUs, Rate, Source  # noqa
from currency.utils import generate_password as gen_pass
from currency.forms import RateForm, SourceForm  # noqa
from currency.tasks import contact_us

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

# Create your views here.


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_delete.html'


class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_details.html'


class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_update.html'


def hello_world(request):
    return render(request, 'home.html')


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source.html'


class SourceCreateView(CreateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_create.html'


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_delete.html'


class SourceDetailView(DetailView):
    queryset = Source.objects.all()
    template_name = 'source_details.html'


class SourceUpdateView(UpdateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_update.html'


def generate_password(request):
    password_len = int(request.GET.get('password-len'))
    password = gen_pass(password_len)
    return HttpResponse(password)


def contactus(request):
    contacts = ContactUs.objects.all()
    context = {
        'contact': contacts,
    }
    return render(request, 'contact.html', context=context)


def response_code(request):
    response = HttpResponse('Status Code', status=200)
    return response


class ContactUsCreateView(CreateView):
    model = ContactUs
    success_url = reverse_lazy('index')
    template_name = 'contactus_create.html'
    fields = (
        'email_from',
        'subject',
        'message',
    )

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        email_from = form.cleaned_data['email_from']

        full_email_body = f'''
        Hello {email_from}
        Message: {message}
        '''
        contact_us.apply_async(args=(subject, ), kwargs={'full_email_body': full_email_body})

        return super().form_valid(form)
