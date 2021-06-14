from django.conf.urls import url
from . import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^submit/expense/$', views.submit_expense, name='submit_expense')

]
