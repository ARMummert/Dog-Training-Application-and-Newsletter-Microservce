from django import forms
from .models import Profile
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
class SubscriberForm(forms.Form):
    email = forms.EmailField(label='Your email',
                             max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
class CreateForm(forms.ModelForm): 
    fullname = forms.CharField(max_length=100, widget=forms.TextInput())
    nickname = forms.CharField(max_length=100, widget=forms.TextInput())
    gender = forms.CharField(max_length=100, widget=forms.TextInput())
    breed = forms.CharField(max_length=50, widget=forms.TextInput())
    age = forms.CharField(max_length=50, widget=forms.TextInput())
    toy = forms.CharField(max_length=100, widget=forms.TextInput())
    image = forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields=('fullname', 'nickname', 'gender', 'breed', 'age', 'toy', 'image')
   

    def __str__(self):
        return self.fullname, self.nickname, self.gender, self.breed, self.age, self.toy, self.image