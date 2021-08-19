import django.forms.widgets as f
import xml.etree.ElementTree as etree
from django.utils.safestring import mark_safe


def make_readonly(form):
    """
    Makes all fields on the form readonly and prevents it from POST hacks.
    """

    def _get_cleaner(_form, field):
        def clean_field():
            return getattr(_form.instance, field, None)
        return clean_field

    for field_name in form.fields.keys():
        form.fields[field_name].widget = ReadOnlyWidget(
            initial_widget=form.fields[field_name].widget)
        setattr(form, "clean_" + field_name,
                _get_cleaner(form, field_name))

    form.is_readonly = True


class ReadOnlyWidget(f.Select):
    """
    Renders the content of the initial widget in a hidden <span>. If the
    initial widget has a ``render_readonly()`` method it uses that as display
    text, otherwise it tries to guess by parsing the html of the initial widget.
    """

    def __init__(self, initial_widget, *args, **kwargs):
        self.initial_widget = initial_widget
        super(ReadOnlyWidget, self).__init__(*args, **kwargs)

    def render(self, *args, **kwargs):
        def guess_readonly_text(original_content):
            root = etree.fromstring("<span>%s</span>" % original_content)

            for element in root:
                if element.tag == 'input':
                    return element.get('value')

                if element.tag == 'select':
                    for option in element:
                        if option.get('selected'):
                            return option.text

                if element.tag == 'textarea':
                    return element.text

            return "N/A"

        original_content = self.initial_widget.render(*args, **kwargs)
        try:
            readonly_text = self.initial_widget.render_readonly(*args, **kwargs)
        except AttributeError:
            readonly_text = guess_readonly_text(original_content)

        return mark_safe("""<span class="hidden">%s</span>%s""" % (
            original_content, readonly_text))
