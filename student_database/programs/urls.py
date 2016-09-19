from django.conf.urls import url

from programs import views


urlpatterns = [
    url(r'^$', views.Programs.as_view(), name='programs'),
]
