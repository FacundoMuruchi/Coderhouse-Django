from django import forms

# FORM USANDO SOLO PYTHON(DJANGO)

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    comision = forms.IntegerField(max_value=50000, required=True)