from django import forms
from django.core.urlresolvers import reverse

from .models import Poster

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button


class AddShowForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
    # call original initializator
        super(AddShowForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('add_show')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-6'

        # form buttons
        self.helper.add_input(Submit('submit', 'Save',css_class='btn-primary'))
        self.helper.add_input(Button('cancel', 'Cancel',css_class='btn',
            onclick="javascript:window.history.back();"))




    class Meta:
        model = Poster
        fields = ('venue', 'show_date', 'show_info', 'tickets_link', 'affiche',)


class EditShowForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
    # call original initializator
        super(EditShowForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('edit_show',
            kwargs={'pk': kwargs['instance'].id})

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-6'

        # form buttons
        self.helper.add_input(Submit('submit', 'Save',css_class='btn-primary'))
        self.helper.add_input(Button('cancel', 'Cancel',css_class='btn',
            onclick="javascript:window.history.back();"))




    class Meta:
        model = Poster
        fields = ('venue', 'show_date', 'show_info', 'tickets_link', 'affiche',)
