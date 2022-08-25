from django import forms

LIGHT_CHOICES=[
        ("Direct light"   ,"Direct light"),
        ("Bright indirect light"   ,"Bright indirect light"),
       ( "Medium light"   ,"Medium light"),
       ( "Low light"   ,"Low Light")]

WATER_CHOICES=[("Let top layer of soil dry between waterings"   ,"Let top layer of soil dry between waterings"), ("Let soil dry completely between waterings","Let soil dry completely between waterings"), ("Keep soil moist","Keep soil moist")]

HUMIDITY_CHOICES=[("High","High"),("Average","Average"),("Dry","Dry")]

SOIL_CHOICES=[
        ( "All-purpose potting mix","All-purpose potting mix"),
        (  "Succulent/cactus mix","Succulent/cactus mix"),
        ("Tropical potting mix","Tropical potting mix"),
        ( "Aroid soilless potting mix","Aroid soilless potting mix"),
        ( "Orchid bark","Orchid bark"),
        ("Perlite/vermiculite","Perlite/vermiculite"),
        ("Coconut coir/peat moss","Coconut coir/peat moss"),
        ( "Sphagnum moss","Sphagnum moss"),
        (  "LECA","LECA"),
        ( "Other/custom blend (see notes)","Other/custom blend (see notes)")]


class PlantForm(forms.Form):
    name = forms.CharField(label='Plant Name', max_length=100, required=False, widget=forms.TextInput
                           (attrs={
                               'required': 'True'
                            }))
    type = forms.CharField(label='Plant Type', max_length=200, required=False, widget=forms.TextInput
                           (attrs={
                               'required': 'True'
                            }))
    light = forms.CharField(label='Sunlight needs', max_length=200, required=False, widget=forms.Select(choices=LIGHT_CHOICES, attrs={
                               'required': 'True'
                            }))
    water = forms.CharField(label='Watering', max_length=200, required=False, widget=forms.Select(choices=WATER_CHOICES, attrs={
                               'required': 'True'
                            }))
    humidity = forms.CharField(label='Humidity needs', max_length=200, required=False, widget=forms.Select(choices=HUMIDITY_CHOICES, attrs={
                               'required': 'True'
                            }))
    soil = forms.CharField(label='Soil',required=False,  widget=forms.Select(choices=SOIL_CHOICES, attrs={
                               'required': 'True'
                            }))
    fertilizer = forms.CharField(label='Fertilizer', max_length=200, required=False, widget=forms.TextInput
                           (attrs={
                               'required': 'True'
                            }))    
    toxicity = forms.BooleanField(label='Check box if the plant is toxic', required=False)
    notes = forms.CharField(label='Notes', max_length=10000, required=False, widget=forms.TextInput
                           (attrs={
                               'required': 'True'
                            }))

# 'Aroid soilless potting mix', 'Orchid bark', 'Perlite/vermiculite', 'Coconut coir/peat moss', 'Sphagnum moss', 'LECA', 'Other/custom blend (see notes)']