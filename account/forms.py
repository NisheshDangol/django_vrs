from django import forms


class ClientRegisterForm(forms.Form):
    email = forms.EmailField(label='email')
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    location = forms.CharField(verbose_name='location', max_length=255)
    phone = forms.IntegerField(verbose_name='phone', null=True)
    pan_vat = forms.ImageField()


class CustomerRegisterForm(forms.Form):
    email = forms.EmailField(verbose_name='email')
    username = forms.CharField(max_length=30, unique='True')
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    location = forms.CharField(verbose_name='location', max_length=255)
    phone = forms.IntegerField(verbose_name='phone', null=True)
    license = forms.ImageField()