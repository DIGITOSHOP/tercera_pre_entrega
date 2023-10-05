from django import forms

class ComentarioForm(forms.Form):
    nombre = forms.CharField(label='Nombre:',max_length=60)
    comentario = forms.CharField (widget=forms.Textarea)