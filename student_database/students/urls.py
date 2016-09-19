from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from students import views


urlpatterns = [
    url(r'^$', login_required(views.Students.as_view()), name='home'),
]
