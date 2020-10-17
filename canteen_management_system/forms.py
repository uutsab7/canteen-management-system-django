from django import forms
from canteen_management_system.models import FoodItem, User, Employee, Cook, Speciality

class FoodForm(forms.Form):

    name = forms.CharField()
    price = forms.IntegerField()
    quantity = forms.IntegerField(min_value=20)
    discount = forms.FloatField(max_value=50)

class FoodModelForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields ='__all__'


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ('name', 'profile_pic', 'age')

class SpecialityModelForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields ='__all__'





