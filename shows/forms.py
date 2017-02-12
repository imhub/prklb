from django import forms
from django.core.urlresolvers import reverse

from .models import Poster

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class AddShowForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
    # call original initializator
        super(AddShowForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('add_show')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-6'

        # form buttons
        self.helper.add_input(Submit('send_button', 'Save'))

    class Meta:
        model = Poster
        fields = ('venue', 'show_date', 'show_info', 'tickets_link', 'affiche',)
