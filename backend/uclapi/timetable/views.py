from django.shortcuts import render
from roombookings.helpers import PrettyJsonResponse as JsonResponse
from timetable.models import TimeTable
# Create your views here.


def get_timetable(request):
    import pdb
    pdb.set_trace()
    print(TimeTable.objects.all())
    return JsonResponse({})
