from django.conf.urls import url
from django.contrib.auth.decorators import login_required


from programs import views


urlpatterns = [
    url(r'^$', login_required(views.Programs.as_view()), name='home'),
]
