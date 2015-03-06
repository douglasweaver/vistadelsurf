from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from datetime import date,datetime
import calendar, time
from django.template import RequestContext
from django.core.mail import send_mail

from .forms import ReservationInquiryForm
import json


from rent.models import Booking, Rate, LEVEL_CHOICES


def year(request, year=None):
	if (request.method == 'POST'):
		contactform = ReservationInquiryForm(request.POST)
		if contactform.is_valid():
			formResults = contactform.cleaned_data

			recipients = ['vistadelsurf@gmail.com']

			subject = 'Reservation Inquiry for ' + formResults['start_date'].isoformat() + ' to ' + formResults['end_date'].isoformat()
			message = (subject + '\n' + 
				'Couples : {:d} Adults: {:d} Children : {:d}'.format(formResults['couples'], formResults['adults'], formResults['children']) +
				'\n' + formResults['message'])

			send_mail(subject, message, formResults['sender'], recipients, fail_silently=True)
			contactform = ReservationInquiryForm()
	else:
		contactform = ReservationInquiryForm()


	lst = Booking.objects.filter(startdate__gte=timezone.now())
	bookdict = {}
	for book in lst:
		for rawday in (book.startdate + timezone.timedelta(n) for n in range((book.enddate-book.startdate).days+1)):
			day = rawday.isoformat()
			bookdict.setdefault( day , [] ).append(book.level)
	
	lst = Rate.objects.filter(enddate__gte=timezone.now()).order_by('-created')
	ratedict = {}
	for rate in lst:
		for rawday in (rate.startdate + timezone.timedelta(n) for n in range((rate.enddate-rate.startdate).days+1)):
			day = rawday.isoformat()
			ratedict.setdefault( day , {} )[rate.level] = rate.rate

	datepickdict = {}
	for day, rdict in ratedict.items() :
		tooltipstr = ""
		numfloors = 0
		if day in bookdict :
			for level, rate in rdict.items() :
				if not level in bookdict[day] :
					numfloors += 1
					tooltipstr += ("" if (tooltipstr == "") else "\n") + level + ': ${:.0f}'.format(rate)
		else :
			for level, rate in rdict.items() :
				numfloors += 1
				tooltipstr += ("" if (tooltipstr == "") else "\n") + level + ': ${:.0f}'.format(rate)
		if tooltipstr != "" :
			datepickdict[day] = {'rate' : tooltipstr, 'style' : 'pct{:d}avail'.format(int(100.0*numfloors/len(LEVEL_CHOICES)))}

	jratelst = json.dumps(datepickdict)
	
	return render(request, 'rent/year.html', dict(form=contactform,
			datepicker_reservation_available_rates=jratelst))
