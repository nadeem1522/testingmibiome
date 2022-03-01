from django import template

register = template.Library()

@register.filter
def beautify(value):
    return value.replace('_', ' ').title()