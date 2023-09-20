from django import forms

class Alimento_Formulario(forms.Form):
    marca = forms.CharField(max_length=200)
    tipo = forms.CharField(max_length=200)
    mascota = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=200)

class Accesorios_Formulario(forms.Form):
    marca = forms.CharField(max_length=200)
    tipo = forms.CharField(max_length=200)
    mascota = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=200)

class Juguetes_Formulario(forms.Form):
    marca = forms.CharField(max_length=200)
    tipo = forms.CharField(max_length=200)
    mascota = forms.CharField(max_length=200)
