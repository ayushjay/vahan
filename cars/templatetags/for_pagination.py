from django import template
register = template.Library()

@register.simple_tag
def fixed_pn(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)

    if urlencode:
        item = urlencode.split('&')
        filtered_item = filter(lambda p: p.split('=')[0]!=field_name, item)
        encoded_item = '&'.join(filtered_item)
        url = '{}&{}'.format(url, encoded_item)

    return url
