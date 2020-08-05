from django import forms


class messagesForm(forms.Form):
    messages = forms.CharField(label="", max_length=100,
                               widget=forms.TextInput(attrs={'class': ' form-control ', 'id': "chat-message-input", 'placeholder': "Enter Message"}))
