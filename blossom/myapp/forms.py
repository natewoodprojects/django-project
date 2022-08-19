from django import forms

class PlantForm(forms.Form):
    name = forms.CharFiels(label='plant_name', max_length=100)
    type = forms.CharField(label='type', max_length=200)
    light = forms.CharField(label='light', max_length=200)
    water = forms.CharField(label='water', max_length=200)
    humidity = forms.CharField(label='humidity', max_length=200)
    soil = forms.CharField(label='soil', max_length=200)
    fertilizer = forms.CharField(label='fertilizer', max_length=200)    
    toxcicity = forms.BooleanField(label='toxcicity')
    notes = forms.CharField(label='notes', max_length=10000)
