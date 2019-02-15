import enum

from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.db import models


class FederativeUnit(models.Model):
    initials = models.CharField('sigla', max_length=2, unique=True)
    name = models.CharField('nome', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'unidade federativa'


class City(models.Model):
    name = models.CharField('nome', max_length=255)
    uf = models.ForeignKey('FederativeUnit', on_delete=models.PROTECT)

    def __str__(self):
        return "{}-{}".format(self.name, self.uf.initials)

    class Meta:
        verbose_name = 'cidade'
        unique_together = (('uf', 'name'),)
        ordering = ('name',)


class Place(models.Model):
    title = models.CharField('título', max_length=255)
    address = models.CharField('endereço', max_length=255)
    city = models.ForeignKey('City', on_delete=models.PROTECT, verbose_name='cidade')
    link_to_map = models.URLField('link para o mapa')
    image = CloudinaryField('imagem', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'local'
        verbose_name_plural = 'locais'


class Source(models.Model):
    description = models.CharField('descrição', max_length=255)
    position = models.SmallIntegerField('posição', default=0, help_text='99 para "Outros"')

    def validate_unique(self, exclude=None):
        if self.position == 99 and \
                Source.objects.exclude(pk=self.pk).filter(position=self.position).exists():
            raise ValidationError('Só deve existir um único registro com a posição igual a "99"')
        super(Source, self).validate_unique(exclude=exclude)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'indicação'
        verbose_name_plural = 'indicações'
        ordering = ('position', 'description')


def get_default_source():
    if Source.objects.filter(position=99).exists():
        return Source.objects.get(position=99)
    else:
        return None


customer_verbose_name = 'cliente'


class Customer(models.Model):
    name = models.CharField('nome completo', max_length=255)
    phone = models.CharField('telefone', max_length=20)
    cpf = models.CharField('CPF', max_length=14)
    rg = models.CharField('RG', max_length=20)
    address = models.CharField('endereço completo', max_length=255, help_text="Rua tal, 123 - Centro")
    cep = models.CharField('CEP', max_length=10)
    city = models.ForeignKey('City', on_delete=models.PROTECT, verbose_name='cidade')
    email = models.EmailField('e-mail', null=True, blank=True)
    profession = models.CharField('profissão', max_length=255, null=True, blank=True)
    age = models.PositiveSmallIntegerField('idade', null=True, blank=True)
    source = models.ForeignKey('Source', on_delete=models.PROTECT, default=get_default_source,
                               verbose_name='como nos conheceu')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = customer_verbose_name
        ordering = ('name',)


class Event(models.Model):
    class EventTypes(enum.Enum):
        treinamento_oratoria = 'tre_ora'
        curso_hipnose = 'cur_hip'
        treinamento_inteligencia_emocional = 'tre_iem'

    title = models.CharField('título', max_length=135)
    subtitle = models.CharField('subtítulo', max_length=120)
    place = models.ForeignKey('Place', on_delete=models.PROTECT, verbose_name='local')
    start_date = models.DateTimeField('data de início')
    end_date = models.DateTimeField('data de término')
    details = models.TextField('detalhes')
    amount = models.DecimalField('valor', max_digits=15, decimal_places=2)
    open_for_subscriptions = models.BooleanField('aberto para inscrições', default=False)
    registrations = models.ManyToManyField('Customer', blank=True, verbose_name='clientes', through='Registration')
    type = models.CharField('tipo', max_length=7, choices=[
        (EventTypes.treinamento_oratoria.value, 'Treinamento de Oratória'),
        (EventTypes.curso_hipnose.value, 'Curso de Hipnose na Prática'),
        (EventTypes.treinamento_inteligencia_emocional.value, 'Treinamento de Inteligência Emocional'),
    ])
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug / URL",
                            help_text="Preenchido automaticamente, não editar.")

    def __str__(self):
        return "{} ({})".format(self.title, self.subtitle)

    class Meta:
        verbose_name = 'evento'


class Registration(models.Model):
    customer = models.ForeignKey('Customer', verbose_name=customer_verbose_name, on_delete=models.PROTECT)
    event = models.ForeignKey('Event', on_delete=models.PROTECT)
    contract_sent = models.BooleanField('contrato enviado?', default=False)

    def __str__(self):
        return '%s [%s]' % (str(self.customer), str(self.event))

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'


class Testimony(models.Model):
    customer = models.ForeignKey('Customer', verbose_name=customer_verbose_name, on_delete=models.PROTECT)
    description = models.TextField('descrição')
    image = CloudinaryField('imagem', help_text="Imagem quadrada com no mínimo 170px")
    visible = models.BooleanField('visível', default=True)

    class Meta:
        verbose_name = 'depoimento'
