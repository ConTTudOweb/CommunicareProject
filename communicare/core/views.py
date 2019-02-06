from django.conf import settings
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse, HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.views.generic import TemplateView, DetailView

from ..core.models import Event, Customer, Registration, Testimony
from ..core.forms import ContactForm, CustomerForm


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        context['events'] = Event.objects.all()
        context['testimonies'] = Testimony.objects.filter(visible=True).all()
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
                                      'Sua mensagem foi cadastrada com sucesso, ' \
                                      'retornaremos o mais rápido possível.'
            response_data['status'] = True

            return JsonResponse(response_data)
        else:
            errors = ""
            for error in form.non_field_errors():
                errors += error
            return JsonResponse({'result': errors, 'status': False})
    else:
        return JsonResponse({"result": "Método inválido! Aceito somente POST."}, status=500)


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

            if customer.email not in [None, '']:
                d = {
                    'event': event,
                    'local': event.place,
                    'customer': customer
                }
                text_content = render_to_string('core/registration_email.txt', d)
                html_content = render_to_string('core/registration_email.html', d)
                subject, to = 'Inscrição efetuada com sucesso!', customer.email

                msg = EmailMultiAlternatives(subject=subject, body=text_content, to=[to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

            return JsonResponse({"results": "Inscrição efetuada com sucesso!"})
        else:
            errors = ""
            for error in form.non_field_errors():
                errors += error
            return JsonResponse({'errors': errors})

    return HttpResponse()


def send_contract(request):
    if request.method == 'GET':
        pk = request.GET.get('pk')
        if Registration.objects.filter(pk=pk).exists():
            registration_obj = Registration.objects.get(pk=pk)

            if registration_obj.customer.email not in [None, '']:
                d = {}
                # d = {
                #     'event': event,
                #     'local': event.place,
                #     'customer': customer
                # }
                text_content = render_to_string('core/contract_email.txt', d)
                html_content = render_to_string('core/contract_email.html', d)
                subject, to = 'Inscrição efetuada com sucesso!', customer.email

                msg = EmailMultiAlternatives(subject=subject, body=text_content, to=[to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

            return JsonResponse({"results": "Inscrição efetuada com sucesso!"})

    return HttpResponse()
