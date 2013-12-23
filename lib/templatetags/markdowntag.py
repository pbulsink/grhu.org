#!/usr/bin/env python
import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def my_markdown(value):
    extensions = ['extra']
    return mark_safe(markdown.markdown(force_unicode(value),
                                       extensions,
                                       safe_mode='remove',
                                       enable_attributes=False))
