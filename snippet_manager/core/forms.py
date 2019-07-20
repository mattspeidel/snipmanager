from django import forms
from django.forms.widgets import Widget
# from core.models import Language
from djangocodemirror.fields import CodeMirrorField

# class codeField(Widget):



class addSnippet(forms.Form):
    title = forms.CharField(max_length=100, min_length=1)
    description = forms.CharField(max_length=500, required=False)
    language = forms.CharField(max_length=50, required=True)
    code = CodeMirrorField(config_name="python", required=False)


class editSnippet(forms.Form):
    title = forms.CharField(max_length=100, min_length=1)
    description = forms.CharField(max_length=500, required=False)
    language = forms.CharField(max_length=50, required=True)
    code = CodeMirrorField(config_name="restructuredtext", required=False)
