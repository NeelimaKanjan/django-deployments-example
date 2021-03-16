from django import template

register = template.Library()

@register.filter(name='cutalpha')
def cut(value,args):
    """This cuts out all values of args from string value"""
    return value.replace(args,'')

# register.filter(filtername,function to be called)
# register.filter('cut',cut)



