from django import forms

SOIL_CHOICES=[('All-purpose potting mix', 'All-purpose potting mix'), ('Succulent/cactus mix', 'Succulent/cactus mix'), ('Tropical potting mix', 'Tropical potting mix')]

class PlantForm(forms.Form):
    name = forms.CharField(label='Plant_name', max_length=100)
    type = forms.CharField(label='Type', max_length=200)
    light = forms.CharField(label='Light', max_length=200)
    water = forms.CharField(label='Water', max_length=200)
    humidity = forms.CharField(label='Humidity', max_length=200)
    soil = forms.CharField(label='Soil', widget=forms.Select(choices=SOIL_CHOICES))
    fertilizer = forms.CharField(label='Fertilizer', max_length=200)    
    toxcicity = forms.BooleanField(label='Toxcicity')
    notes = forms.CharField(label='Notes', max_length=10000)

# 'Aroid soilless potting mix', 'Orchid bark', 'Perlite/vermiculite', 'Coconut coir/peat moss', 'Sphagnum moss', 'LECA', 'Other/custom blend (see notes)']