from django.conf.urls import url
from . import views

app_name = "mapa"

urlpatterns = [

    url(r'^$',views.tabla,name='tabla'),


]
