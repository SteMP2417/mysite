from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view,name='index'),
    path('About', about_view,name='about'),
    path('Contact', contact_view,name='contact'),
    
]
