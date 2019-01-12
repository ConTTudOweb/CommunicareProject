from django.core.exceptions import ValidationError
from django.db import models


class FederativeUnit(models.Model):
    initials = models.CharField('sigla', max_length=2)
    name = models.CharField('nome', max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField('nome', max_length=255)
    uf = models.ForeignKey('FederativeUnit', on_delete=models.PROTECT)

    def __str__(self):
        return "{}-{}".format(self.name, self.uf.initials)

    class Meta:
        verbose_name = 'cidade'


class Place(models.Model):
    title = models.CharField('título', max_length=255)
    address = models.CharField('endereço', max_length=255)
    city = models.ForeignKey('City', on_delete=models.PROTECT, verbose_name='cidade')
    link_to_map = models.URLField('link para o mapa')

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

    class Meta:
        verbose_name = 'indicação'
        verbose_name_plural = 'indicações'
        ordering = ('position', 'description')


def get_default_source():
    return Source.objects.get(position=99)


class Customer(models.Model):
    name = models.CharField('nome completo', max_length=255)
    phone = models.CharField('telefone', max_length=20)
    cpf = models.CharField('CPF', max_length=14)
    rg = models.CharField('RG', max_length=20)
    address = models.CharField('endereço completo', max_length=255)
    cep = models.CharField('CEP', max_length=10)
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    email = models.EmailField(null=True, blank=True)
    profession = models.CharField('profissão', max_length=255, null=True, blank=True)
    age = models.PositiveSmallIntegerField('idade', null=True, blank=True)
    source = models.ForeignKey('Source', on_delete=models.PROTECT, default=get_default_source)

    class Meta:
        verbose_name = 'cliente'


class Event(models.Model):
    title = models.CharField('título', max_length=255)
    subtitle = models.CharField('subtítulo', max_length=255)
    place = models.ForeignKey('Place', on_delete=models.PROTECT, verbose_name='local')
    start_date = models.DateTimeField('data de início')
    end_date = models.DateTimeField('data de término')
    details = models.TextField('detalhes')
    open_for_subscriptions = models.BooleanField('aberto para inscrições', default=False)
    registrations = models.ManyToManyField('Customer', blank=True, verbose_name='clientes')

    def __str__(self):
        return "{} ({})".format(self.title, self.subtitle)

    class Meta:
        verbose_name = 'evento'
