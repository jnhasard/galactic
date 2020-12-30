from django import forms


class MyForm(forms.Form):
    info = forms.CharField(widget=forms.Textarea(
        attrs={"rows": 16, "cols": 60}), label="")
