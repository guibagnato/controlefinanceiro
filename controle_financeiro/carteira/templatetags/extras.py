from django import template

register = template.Library()

@register.filter
def to_percent(value):
    value = float(value) * 100
    return '{} %'.format(round(value, 2))