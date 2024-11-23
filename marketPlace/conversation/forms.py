from django import forms
from.models import ConversationMessage



class conversationMessageForm(forms.ModelForm):
    class Meta:
     
     model=ConversationMessage
     fields=('content',)
     widget={
        'content':forms.Textarea(attrs={
           'class':'w-full py-4 px-6 rounded-xl border'
        })
     }
