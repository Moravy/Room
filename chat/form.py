from django import forms


class userForm(forms.Form):
    userName = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={'class': 'username form-control', 'id': 'username', 'placeholder': "Enter Username"}))
