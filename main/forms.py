from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full bg-gray-800 px-4 py-3 rounded-lg',
            'placeholder': 'Votre nom'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full bg-gray-800 px-4 py-3 rounded-lg',
            'placeholder': 'votre@email.com'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full bg-gray-800 px-4 py-3 rounded-lg',
            'placeholder': 'Votre message',
            'rows': 5
        })
    )
