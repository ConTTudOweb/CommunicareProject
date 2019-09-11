import re

from django.utils.safestring import mark_safe


def get_whatsapp_link(phone):
    if not phone:
        return ""

    img_whatsapp = '<img style="height: 1rem;" src="https://img.icons8.com/color/48/000000/whatsapp.png">'
    api = 'https://api.whatsapp.com/send?phone='
    a_link = '<a target="_blank" href="{}55{}">{}</a>'.format(
        api,
        re.sub("[^0-9]", "", phone),
        img_whatsapp
    )
    return mark_safe(a_link)
