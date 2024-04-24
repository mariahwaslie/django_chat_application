from django import forms
from .models import ChatGroup,Message

class GroupForm(forms.ModelForm):
    class Meta:
        model= ChatGroup
        fields = ['name','description']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].label = 'Name The Chat Room'
            self.fields['description'].label = 'Give a description of the Chat Room'
