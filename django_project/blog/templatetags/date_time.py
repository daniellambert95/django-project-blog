from django import template
from datetime import date

register = template.Library()

@register.simple_tag(name='the_date')
def the_date():
    today = date.today()
    date_today = str(today.strftime("%B %d, %Y"))
    return date_today