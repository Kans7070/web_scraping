from django import forms


class ScraperInputForm(forms.Form):

    url = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control col-12 mb-3',
        'placeholder': 'put url here',
        
    }), label='')

    class Meta:
        fields = ['url']