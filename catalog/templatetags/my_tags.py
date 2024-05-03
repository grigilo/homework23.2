from django import template

register = template.Library()


@register.simple_tag()
def image_tag(path):
    if path:
        return f"/media/{path}"
    return "#"
