from django.forms import ModelForm
#from .models import Details

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'



class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
