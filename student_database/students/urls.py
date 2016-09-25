from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from students import views


urlpatterns = [
    url(r'^$', login_required(views.Students.as_view()), name='students-list'),
    url(r'^create/$',
        login_required(views.StudentCreate.as_view()),
        name='create'),
    url(r'^create/(?P<student_id>[0-9]+)/$',
        login_required(views.StaffContactCreate.as_view()),
        name='create'),
    url(r'^update/(?P<pk>[0-9]+)/$',
        login_required(views.StudentUpdate.as_view()),
        name='update'),
]
