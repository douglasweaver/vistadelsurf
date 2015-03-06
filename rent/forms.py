from django import forms
from django.forms.widgets import NumberInput
from functools import partial

ReservationStartInput = partial(forms.DateInput, {'id': 'datepicker_reservation_from'})

ReservationEndInput = partial(forms.DateInput, {'id': 'datepicker_reservation_to'})

class ReservationInquiryForm(forms.Form):
	start_date = forms.DateField(widget=ReservationStartInput(),error_messages={'required': 'Please select a check-in date'})
	end_date = forms.DateField(widget=ReservationEndInput(),error_messages={'required': 'Please select a check-out date'})
	couples = forms.IntegerField(min_value=0,required=False,initial=0)
	adults = forms.IntegerField(min_value=0,required=False,initial=0)
	children = forms.IntegerField(min_value=0,required=False,initial=0)
	message = forms.CharField(widget=forms.Textarea(attrs={'rows': 7 }),required=False)
	sender = forms.EmailField(error_messages={'required': 'Please specify your email address'})
