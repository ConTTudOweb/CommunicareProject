from django import forms
from django.core.exceptions import ValidationError

from communicare.core.models import Customer


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail', required=False)
    phone = forms.CharField(label='Telefone', required=False)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'rows': 2}))

    def clean(self):
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')

        return self.cleaned_data


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
