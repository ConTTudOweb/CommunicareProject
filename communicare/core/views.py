from datetime import datetime

from django.conf import settings
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView, DetailView, FormView

from communicare.core.context_processors import PAGES
from ..core.forms import ContactForm, CustomerForm, InterestedForm, WaitlistedForm, LeadForm
from ..core.models import Event, Customer, Registration, Testimony, WaitingList, EventTypes, Gallery, \
    TestimonyHipnoterapia


def get_current_event(type):
    return Event.objects.filter(start_date__gt=datetime.now(), open_for_subscriptions=True, visible=True, type=type)\
        .order_by('start_date').first()


def get_current_waiting_list(type):
    return WaitingList.objects.filter(type=type).first()


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


def contact_whatsapp(request):
    response_data = {}
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            from_ = str(settings.DEFAULT_FROM_EMAIL),

            message = "Nova solicitação de contato por whatsapp feita no site!\nNome: {name}\nWhatsapp: {phone}\nE-mail: {email}".format(
                name=form.instance.name,
                phone=form.instance.phone,
                email=form.instance.email,
            )
            email = mail.EmailMessage(
                subject='Me chame no whatsapp ({})'.format(form.instance.name),
                body=message,
                to=from_
            )
            email.send()
            response_data['result'] = 'Obrigado pelo seu contato!<br>' \
                                      'Retornaremos o mais rápido possível.'
            response_data['status'] = True
        else:
            errors = ""
            for error in form.non_field_errors():
                errors += error
            for error in form.errors:
                errors += form.errors[error]
            response_data['result'] = errors
            response_data['status'] = False

        return JsonResponse(response_data)
    else:
        return JsonResponse({"result": "Método inválido! Aceito somente POST."}, status=500)


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
            # event.registrations.add(customer, through_defaults={'contract_sent': False})
            Registration.objects.create(
                customer=customer,
                event=event
            )

            # if customer.email not in [None, '']:
            d = {
                'event': event,
                'local': event.place,
                'customer': customer
            }
            text_content = render_to_string('core/registration_email.txt', d)
            html_content = render_to_string('core/registration_email.html', d)
            subject = 'Inscrição efetuada com sucesso! (%s)' % customer.name
            to = customer.email
            msg = EmailMultiAlternatives(subject=subject, body=text_content, to=[to], cc=[str(settings.DEFAULT_FROM_EMAIL)])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return JsonResponse({"results": "Inscrição efetuada com sucesso!"})
        else:
            errors = ""
            for error in form.non_field_errors():
                errors += error
            return JsonResponse({'errors': errors})

    return HttpResponse()


def waitlisted(request):
    if request.method == 'POST':
        form = WaitlistedForm(request.POST)
        if form.is_valid():
            form.save()
            # event = Event.objects.get(pk=request.POST.get('event_id'))
            # Registration.objects.create(
            #     customer=customer,
            #     event=event
            # )

            # if customer.email not in [None, '']:
            d = {
                'waitlisted': form.instance
            }
            text_content = render_to_string('core/waitlisted_email.txt', d)
            html_content = render_to_string('core/waitlisted_email.html', d)
            subject = 'Inscrição para a lista de espera efetuada com sucesso! (%s)' % form.instance.name
            to = form.instance.email
            msg = EmailMultiAlternatives(subject=subject, body=text_content, to=[to], cc=[str(settings.DEFAULT_FROM_EMAIL)])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return JsonResponse({"results": "Inscrição na lista de espera efetuada com sucesso!"})
        else:
            errors = ""
            for error in form.non_field_errors():
                errors += error
            return JsonResponse({'errors': errors})

    return HttpResponse()


def interested(request, type, title):
    if request.method == 'POST':
        form = InterestedForm(request.POST)
        if form.is_valid():
            d = {
                'form': form.cleaned_data,
                'type': type,
                'title': title
            }
            text_content = render_to_string('core/interested_email.txt', d)
            html_content = render_to_string('core/interested_email.html', d)
            subject = 'Novo interessado em %s. (%s)' % (type, form.cleaned_data['name'])
            to = settings.DEFAULT_FROM_EMAIL
            msg = EmailMultiAlternatives(subject=subject, body=text_content, to=[to],
                                         reply_to=[form.cleaned_data['email']])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return JsonResponse({
                "results": "Seu interesse foi registrado com sucesso!<br>Em breve entraremos em contato."})
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
                d = {
                    'event': registration_obj.event,
                    'customer': registration_obj.customer
                }
                text_content = render_to_string('core/contract_email.txt', d)
                html_content = render_to_string('core/contract_email.html', d)
                subject, to = 'Contrato ({})' % registration_obj.event.title, registration_obj.customer.email

                msg = EmailMultiAlternatives(subject=subject, body=text_content, to=[to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

            return JsonResponse({"results": "Contrato enviado com sucesso!"})

    return HttpResponse()


# class CertificateTemplateView(TemplateView):
#     template_name = "core/certificate.html"
#
#
# class ContractTemplateView(TemplateView):
#     template_name = "core/contract.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(ContractTemplateView, self).get_context_data(**kwargs)
#         context['registration'] = Registration.objects.get(pk=2)
#         return context


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        context['events'] = Event.objects.filter(visible=True).order_by('start_date')
        context['event_treinamento_oratoria'] = get_current_event(EventTypes.treinamento_oratoria.value)
        context['waiting_list_treinamento_oratoria'] = get_current_waiting_list(EventTypes.treinamento_oratoria.value)
        context['event_curso_hipnose'] = get_current_event(EventTypes.curso_hipnose.value)
        context['waiting_list_curso_hipnose'] = get_current_waiting_list(EventTypes.curso_hipnose.value)
        context['event_treinamento_inteligencia_emocional'] = get_current_event(EventTypes.treinamento_inteligencia_emocional.value)
        context['waiting_list_treinamento_inteligencia_emocional'] = get_current_waiting_list(EventTypes.treinamento_inteligencia_emocional.value)
        context['testimonies'] = Testimony.objects.filter(visible=True).all()
        # SEO
        context['page'] = PAGES.get("PAGE_HOME")
        return context


class EventDetailView(DetailView):
    model = Event
    template_name = "event_register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer_form'] = CustomerForm
        context['event_types'] = EventTypes.__members__
        # SEO
        context['page'] = PAGES.get("PAGE_GENERICA")
        return context


class WaitingListDetailView(DetailView):
    model = WaitingList
    template_name = "waiting-list_register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['waitlisted_form'] = WaitlistedForm
        context['event_types'] = EventTypes.__members__
        # SEO
        context['page'] = PAGES.get("PAGE_GENERICA")
        return context


class InterestedFormView(FormView):
    # template_name = "interested_form.html"
    form_class = InterestedForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # SEO
        context['page'] = PAGES.get("PAGE_GENERICA")
        return context


class InterestedEmotionalIntelligenceLecture(InterestedFormView):
    template_name = "interested_form_palestra_inteligencia_emocional.html"


class InterestedHypnotherapy(InterestedFormView):
    template_name = "interested_form_atendimento_hipnoterapia.html"


# class InterestedCoaching(InterestedFormView):
#     template_name = "interested_form_atendimento_coaching.html"


class BaseTemplateView(TemplateView):
    page_context = PAGES.get("PAGE_GENERICA")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # SEO
        context['page'] = self.page_context
        return context


class PrivacyPolicyTemplateView(BaseTemplateView):
    template_name = 'privacy_policy.html'


class CookiesStatementTemplateView(BaseTemplateView):
    template_name = 'cookies_statement.html'


class GalleryTemplateView(BaseTemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryTemplateView, self).get_context_data(**kwargs)
        context['images'] = Gallery.objects.all()
        return context


class BaseCursoTemplateView(TemplateView):
    event_type = None
    page = None

    def get_context_data(self, **kwargs):
        context = super(BaseCursoTemplateView, self).get_context_data(**kwargs)
        if self.event_type:
            context['event'] = get_current_event(self.event_type.value)
            context['waiting_list'] = get_current_waiting_list(self.event_type.value)
            context['event_type'] = self.event_type.value
        # SEO
        context['page'] = PAGES.get(self.page)
        return context


class TreinamentoOratoriaTemplateView(BaseCursoTemplateView):
    template_name = 'treinamento_oratoria.html'
    event_type = EventTypes.treinamento_oratoria
    page = "PAGE_TREINAMENTO_ORATORIA"


class CursoHipnoseTemplateView(BaseCursoTemplateView):
    template_name = 'curso_hipnose.html'
    event_type = EventTypes.curso_hipnose
    page = "PAGE_CURSO_HIPNOSE"


class TreinamentoInteligenciaEmocionalTemplateView(BaseCursoTemplateView):
    template_name = 'treinamento_inteligencia_emocional.html'
    event_type = EventTypes.treinamento_inteligencia_emocional
    page = "PAGE_TREINAMENTO_INTELIGENCIA_EMOCIONAL"


# class AtendimentoCoachingTemplateView(BaseCursoTemplateView):
#     template_name = 'atendimento_coaching.html'
#     page = "PAGE_ATENDIMENTO_COACHING"


class AtendimentoHipnoterapiaTemplateView(BaseCursoTemplateView):
    template_name = 'atendimento_hipnoterapia.html'
    page = "PAGE_ATENDIMENTO_HIPNOTERAPIA"

    def get_context_data(self, **kwargs):
        context = super(AtendimentoHipnoterapiaTemplateView, self).get_context_data(**kwargs)
        context['testimonies'] = TestimonyHipnoterapia.objects.all()
        return context


class BasePalestraTemplateView(TemplateView):
    page = None

    def get_context_data(self, **kwargs):
        context = super(BasePalestraTemplateView, self).get_context_data(**kwargs)
        # SEO
        context['page'] = PAGES.get(self.page)
        return context


class PalestraInteligenciaEmocionalTemplateView(BasePalestraTemplateView):
    template_name = 'palestra_inteligencia_emocional.html'
    page = "PAGE_PALESTRA_INTELIGENCIA_EMOCIONAL"
