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
source_verbose_name = 'como nos conheceu'


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
                               verbose_name=source_verbose_name)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = customer_verbose_name
        ordering = ('name',)


event_verbose_name = 'evento'


class EventTypes(enum.Enum):
    treinamento_oratoria = 'tre_ora'
    curso_hipnose = 'cur_hip'
    treinamento_inteligencia_emocional = 'tre_iem'


def GetEventTypesDisplay(str):
    if str == EventTypes.treinamento_oratoria.value:
        return 'Treinamento de Oratória'
    elif str == EventTypes.curso_hipnose.value:
        return 'Curso de Hipnose Clínica'
    elif str == EventTypes.treinamento_inteligencia_emocional.value:
        return 'Treinamento de Inteligência Emocional'


class Event(models.Model):
    title = models.CharField('título', max_length=135)
    subtitle = models.CharField('subtítulo', max_length=120)
    place = models.ForeignKey('Place', on_delete=models.PROTECT, verbose_name='local')
    start_date = models.DateTimeField('data de início')
    end_date = models.DateTimeField('data de término')
    details = models.TextField('detalhes')
    amount = models.DecimalField('valor', max_digits=15, decimal_places=2, null=True, blank=True)
    amount_lote1 = models.DecimalField('valor lote 1', max_digits=15, decimal_places=2, null=True, blank=True)
    start_date_lote1 = models.DateTimeField('data de início lote 1', null=True, blank=True)
    end_date_lote1 = models.DateTimeField('data de término lote 1', null=True, blank=True)
    amount_lote2 = models.DecimalField('valor lote 2', max_digits=15, decimal_places=2, null=True, blank=True)
    start_date_lote2 = models.DateTimeField('data de início lote 2', null=True, blank=True)
    end_date_lote2 = models.DateTimeField('data de término lote 2', null=True, blank=True)
    amount_lote3 = models.DecimalField('valor lote 3', max_digits=15, decimal_places=2, null=True, blank=True)
    start_date_lote3 = models.DateTimeField('data de início lote 3', null=True, blank=True)
    end_date_lote3 = models.DateTimeField('data de término lote 3', null=True, blank=True)
    visible = models.BooleanField('visível no site', default=True)
    open_for_subscriptions = models.BooleanField('aberto para inscrições', default=False)
    registrations = models.ManyToManyField('Customer', blank=True, verbose_name='clientes', through='Registration')
    type = models.CharField('tipo', max_length=7, choices=[
        (EventTypes.treinamento_oratoria.value, GetEventTypesDisplay(EventTypes.treinamento_oratoria.value)),
        (EventTypes.curso_hipnose.value, GetEventTypesDisplay(EventTypes.curso_hipnose.value)),
        (EventTypes.treinamento_inteligencia_emocional.value,
         GetEventTypesDisplay(EventTypes.treinamento_inteligencia_emocional.value)),
    ])
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug / URL",
                            help_text="Preenchido automaticamente, não editar.")

    def __str__(self):
        return "{} ({})".format(self.title, self.subtitle)

    class Meta:
        verbose_name = event_verbose_name


class Registration(models.Model):
    class NfStatus(enum.Enum):
        null = ''
        pendente = 'P'
        emitida = 'E'
    customer = models.ForeignKey('Customer', verbose_name=customer_verbose_name, on_delete=models.PROTECT)
    event = models.ForeignKey('Event', verbose_name=event_verbose_name, on_delete=models.PROTECT)
    contract_sent = models.BooleanField('contrato enviado?', default=False)
    financial_generated = models.BooleanField('financeiro gerado?', default=False)
    financial_observations = models.TextField('observações financeiras', null=True, blank=True)
    nf_status = models.CharField('Situação NF', max_length=1, blank=True, default=NfStatus.pendente.value, choices=[
        (NfStatus.null.value, ''),
        (NfStatus.pendente.value, 'Pendente'),
        (NfStatus.emitida.value, 'Emitida'),
    ])
    nf = models.CharField('NF', max_length=60, null=True, blank=True)
    net_value = models.DecimalField('valor líquido', max_digits=15, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return '%s [%s]' % (str(self.customer), str(self.event))

    class Meta:
        verbose_name = 'inscrito'


class Testimony(models.Model):
    customer = models.ForeignKey('Customer', verbose_name=customer_verbose_name, on_delete=models.PROTECT)
    description = models.TextField('descrição')
    image = CloudinaryField('imagem', help_text="Imagem quadrada com no mínimo 170px")
    visible = models.BooleanField('visível', default=True)

    def __str__(self):
        return str(self.customer)

    class Meta:
        verbose_name = 'depoimento'


class WaitingList(models.Model):
    type = models.CharField('tipo', max_length=7, choices=[
        (EventTypes.treinamento_oratoria.value, GetEventTypesDisplay(EventTypes.treinamento_oratoria.value)),
        (EventTypes.curso_hipnose.value, GetEventTypesDisplay(EventTypes.curso_hipnose.value)),
        (EventTypes.treinamento_inteligencia_emocional.value, GetEventTypesDisplay(EventTypes.treinamento_inteligencia_emocional.value)),
    ])
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug / URL",
                            help_text="Preenchido automaticamente, não editar.")

    def __str__(self):
        return "{}".format(self.get_type_display())

    class Meta:
        verbose_name = 'lista de espera'
        verbose_name_plural = 'listas de espera'


class Waitlisted(models.Model):
    name = models.CharField('nome completo', max_length=255)
    phone = models.CharField('telefone', max_length=20)
    email = models.EmailField('e-mail', null=True, blank=True)
    city = models.ForeignKey('City', on_delete=models.PROTECT, verbose_name='cidade')
    waiting_list = models.ForeignKey('WaitingList', on_delete=models.PROTECT)

    def __str__(self):
        return '%s [%s]' % (self.name, str(self.waiting_list))

    class Meta:
        verbose_name = 'interessado'


class Expense(models.Model):
    description = models.CharField('descrição', max_length=255)
    amount = models.DecimalField('valor', max_digits=15, decimal_places=2, null=True, blank=True)
    event = models.ForeignKey('Event', verbose_name=event_verbose_name, on_delete=models.PROTECT)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'despesa'
