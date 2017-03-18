from django import forms
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from .models import Video

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button

class AddVideoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
    # call original initializator
        super(AddVideoForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('add_video')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-6'

        # form buttons
        self.helper.add_input(Submit('submit_button', _('Save'),
            css_class='btn-success'))
        self.helper.add_input(Button('cancel_button', _('Cancel'),css_class='btn',
            onclick="javascript:window.history.back();"))


    class Meta:
        model = Video
        fields = ('title', 'notes', 'vid',)


class EditVideoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
    # call original initializator
        super(EditVideoForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('edit_video',
            kwargs={'pk': kwargs['instance'].id})

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-6'

        # form buttons
        self.helper.add_input(Submit('submit', _('Save'),
            css_class='btn-success'))
        self.helper.add_input(Button('cancel', _('Cancel'),css_class='btn',
            onclick="javascript:window.history.back();"))


    class Meta:
        model = Video
        fields = ('title', 'notes', 'vid',)
