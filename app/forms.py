from django.forms import ModelForm
from .models import Question
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 
 
class addQuesform(ModelForm):
    class Meta:
        model=Question
        fields="__all__"