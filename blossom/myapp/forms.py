from django import forms

SOIL_CHOICES=[('All-purpose potting mix', 'All-purpose potting mix'), ('Succulent/cactus mix', 'Succulent/cactus mix'), ('Tropical potting mix', 'Tropical potting mix')]

class PlantForm(forms.Form):
    name = forms.CharField(label='Plant_name', max_length=100, required=False, widget=forms.TextInput
                           (attrs={
                               'required': 'True'
                            }))
    type = forms.CharField(label='Type', max_length=200, required=False, widget=forms.TextInput
                           (attrs={
                               'required': 'True'
                            }))
    light = forms.CharField(label='Light', max_length=200, required=False, widget=forms.TextInput
                           (attrs={
                               'required': 'True'
                            }))
    water = forms.CharField(label='Water', max_length=200, required=False, widget=forms.TextInput
                           (attrs={
                               'required': 'True'
                            }))
    humidity = forms.CharField(label='Humidity', max_length=200, required=False, widget=forms.TextInput
                           (attrs={
                               'required': 'True'
                            }))
    soil = forms.CharField(label='Soil',required=False,  widget=forms.Select(choices=SOIL_CHOICES, attrs={
                               'required': 'True'
                            }))
    fertilizer = forms.CharField(label='Fertilizer', max_length=200, required=False, widget=forms.TextInput
                           (attrs={
                               'required': 'True'
                            }))    
    toxcicity = forms.BooleanField(label='Toxcicity', required=False)
    notes = forms.CharField(label='Notes', max_length=10000, required=False, widget=forms.TextInput
                           (attrs={
                               'required': 'True'
                            }))

# 'Aroid soilless potting mix', 'Orchid bark', 'Perlite/vermiculite', 'Coconut coir/peat moss', 'Sphagnum moss', 'LECA', 'Other/custom blend (see notes)']