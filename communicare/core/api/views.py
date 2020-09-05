from django.conf import settings
from django.core import mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet

from .serializers import EventSerializer, TestimonySerializer, ContactSerializer, TestimonyHipnoterapiaSerializer
from ..models import Event, Testimony, TestimonyHipnoterapia


class EventViewSet(ReadOnlyModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.filter(visible=True).order_by('start_date')


class TestimonyViewSet(ReadOnlyModelViewSet):
    serializer_class = TestimonySerializer
    queryset = Testimony.objects.filter(visible=True).all()


class TestimonyHipnoterapiaViewSet(ReadOnlyModelViewSet):
    serializer_class = TestimonyHipnoterapiaSerializer
    queryset = TestimonyHipnoterapia.objects.all()


class ContactViewSet(ViewSet):
    permission_classes = []
    serializer_class = ContactSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # send email using the request.POST dictionary
        to = serializer.data.get('email')
        from_ = str(settings.DEFAULT_FROM_EMAIL),
        message = "{name} / {email} / {phone} disse: ".format(
            name=serializer.data.get('name'),
            email=to,
            phone=serializer.data.get('phone'),
        )
        message += "\n\n{0}".format(serializer.data.get('message'))
        email = mail.EmailMessage(
            subject='Contato pelo site.',
            body=message,
            to=from_,
            reply_to=[to],
        )
        email.send()

        response_data = {
            'result': 'Obrigado pelo seu contato!<br>'
                      'Sua mensagem foi cadastrada com sucesso, retornaremos o mais rápido possível.'
        }

        return Response(data=response_data, status=status.HTTP_201_CREATED)
