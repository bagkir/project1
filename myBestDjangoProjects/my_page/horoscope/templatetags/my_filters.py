from django import template

register = template.Library()


@register.filter(name='split')
def split(value, key=' '):
    return value.split(key)[0]


@register.filter(name='make_list')
def make_list(value):
    return range(value)


@register.filter(name='filter_range')
def filter_range(value1, value2):
    return range(int(value1), int(value2))