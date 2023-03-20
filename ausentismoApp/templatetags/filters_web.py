from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()


@register.filter
def prepend_dollars(dollars):
    if dollars:
        dollars = round(float(dollars), 2)
        return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])
    else:
        return "$ 0.00"


@register.filter
def prepend_time(time):
    if time:
        return time
    else:
        return "00:00"


@register.filter
def prepend_hours(hours):
    if hours:
        hours = hours.strftime("%H:%M")
        return "%s" % (hours)
    else:
        return ""


@register.filter(name="placeholder")
def placeholder(value, token):
    value.field.widget.attrs["placeholder"] = token
    return value
