from django import template
from django.utils.safestring import mark_safe
from .stroke_icons import icons
import re

register = template.Library()

@register.simple_tag
def hgi_stroke(name="", size="24", color="#000000", stroke_width="2"):

	if name == "":
		return ""
	
	selected_svg = icons[name].strip()

	if selected_svg == "":
		return ""
	

	selected_svg = re.sub('(\s+|\n)', ' ', selected_svg)

	## remove all quotes and return the element
	return mark_safe(selected_svg.format(**{
		'height': size,
		'width': size,
		'stroke_width': stroke_width,
		'color': color
	}).replace('\n', ''))