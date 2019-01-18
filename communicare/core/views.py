from django.conf import settings
from django.core import mail
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView, DetailView

from ..core.models import Event, Customer
from ..core.forms import ContactForm, CustomerForm


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        context['events'] = Event.objects.all()
        return context


def contact(request):
    response_data = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email using the request.POST dictionary
            to = request.POST.get('email')
            from_ = str(settings.DEFAULT_FROM_EMAIL),

            message = "{name} / {email} / {phone} disse: ".format(
                name=request.POST.get('name'),
                email=to,
                phone=request.POST.get('phone'),
            )
            message += "\n\n{0}".format(request.POST.get('message'))
            email = mail.EmailMessage(
                subject='Contato pelo site.',
                body=message,
                to=from_,
                reply_to=[to],
            )
            email.send()
            response_data['result'] = 'Obrigado pelo seu contato!<br>' \
                                      'O interesse pelo curso foi cadastrado com sucesso, ' \
                                      'retornaremos o mais rápido possível.'

            return JsonResponse(response_data)
        else:
            errors = ""
            for error in form.non_field_errors():
                errors += error
            return JsonResponse({'result': errors})
    else:
        return JsonResponse({"result": "Método inválido! Aceito somente POST."})


class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer_form'] = CustomerForm
        return context


def registration(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            if not Customer.objects.filter(cpf=form.instance.cpf).exists():
                form.save()
                customer = form.instance
            else:
                customer = Customer.objects.filter(cpf=form.instance.cpf).first()
                form.instance.id = customer.id
                form.save()
            event = Event.objects.get(pk=request.POST.get('event_id'))
            event.registrations.add(customer)
            return JsonResponse({"results": "Inscrição efetuada com sucesso!"})
        else:
            errors = ""
            for error in form.non_field_errors():
                errors += error
            return JsonResponse({'errors': errors})

    return HttpResponse()
