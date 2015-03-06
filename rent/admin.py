from django.contrib import admin
from rent.models import Booking, Rate

class BookingAdmin(admin.ModelAdmin):
 #   fieldsets = [
 #                (None,               {'fields': ['title']}),
 #                ('Date information', {'fields': ['date','created'], 'classes': ['collapse']}),
 #   ]
    list_display = ('title', 'startdate', 'enddate', 'was_created_recently')
    list_filter = ['startdate','enddate', 'created']
    search_fields = ['title']

admin.site.register(Booking, BookingAdmin)

class RateAdmin(admin.ModelAdmin):

    list_display = ('title', 'level', 'startdate', 'enddate')
    list_filter = ['startdate','enddate', 'level', 'created']
    search_fields = ['title', 'level']

admin.site.register(Rate, RateAdmin)
