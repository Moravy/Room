from django import forms


class roomForm(forms.Form):
    room_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'class': 'roomForm form-control', 'id': 'roomForm', 'placeholder': "Enter Room"}))
