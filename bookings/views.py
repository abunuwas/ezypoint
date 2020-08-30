import datetime
import json

from django.shortcuts import render

# Create your views here.


def index(request):
    services = [
       {
           'service': 'Head shave',
           'time': 15,
           'selected': False
       },
       {
           'service': 'Dry cut',
           'time': 30,
           'selected': False
       },
       {
           'service': 'Wash and cut',
           'time': 45,
           'selected': False
       },
       {
           'service': 'Skin fade',
           'time': 45,
           'selected': False
       },
       {
           'service': 'Women\'s cut',
           'time': 45,
           'selected': False
       },
    ]
    
    staff = [
       {
           'name': 'John Wayne',
           'available': True,
           'selected': False
       },
       {
           'name': 'Clint Eastwood',
           'available': True,
           'selected': False
       },
       {
           'name': 'Chuck Norris',
           'available': False,
           'selected': False
       },
       {
           'name': 'Arnold Schwarzenegger',
           'available': True,
           'selected': False
       },
       {
           'name': 'Sylvester Stallone',
           'available': True,
           'selected': False
       }
    ]

    return render(
        request, 'bookings/appointments.html',
        context={
            'services': json.dumps(services),
            'staff': json.dumps(staff),
        }
    )
