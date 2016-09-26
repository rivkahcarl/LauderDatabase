from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from programs import views


urlpatterns = [
    url(r'^$',
        login_required(views.Programs.as_view()),
        name='programs-list'),
    url(r'^create$',
        login_required(views.ProgramCreate.as_view()),
        name='create'),
    url(r'^add-students/(?P<pk>[0-9]+)/$',
        login_required(views.AddStudents.as_view()),
        name='add-students'),
    url(r'^update/(?P<pk>[0-9]+)/$',
        login_required(views.ProgramUpdate.as_view()),
        name='update'),
]
