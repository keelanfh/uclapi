from django.conf.urls import url

from timetable.views import get_timetable

urlpatterns = [
    url(r'get/', get_timetable),
]
