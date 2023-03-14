from django import template

register = template.Library()


@register.filter
def task_status(task):
    if task.completed:
        return "Completed"
    else:
        return "Incomplete"


@register.filter
def task_status_icon(task):
    if task.completed:
        return "check_circle"
    else:
        return "radio_button_unchecked"


@register.simple_tag
def url_replace(request, field, value):
    """
    Returns the URL query string with the given field set to the given value.
    """
    url_dict = request.GET.copy()
    url_dict[field] = str(value)
    return url_dict.urlencode()
