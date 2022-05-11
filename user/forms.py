from django.forms import ModelForm
from creator.models import CreatorDetails

class CreatorDetailsForm(ModelForm):
    class Meta:
        model = CreatorDetails
        fields = ['name', 'profile_photo', 'cover_photo', 'slug', 'about']#'__all__'