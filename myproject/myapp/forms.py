from django import forms


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Логин",
                               widget=forms.TextInput(
                                   attrs={'class': 'form-input', 'placeholder': 'Введите свой логин'}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-input', 'placeholder': 'Введите свой пароль'}))
