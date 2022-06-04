from django.urls import path
from .views import *

app_name = 'app.urls'

urlpatterns = [
    path('', home, name="home"),
    path('download', download, name='download'),
    path('contact-us', ContactUs, name='contact-us'),
    path('privacy-policy', PrivayPolicy, name="privacy-policy"),
    path('terms-of-service', TermsOfService, name="terms-of-service"),
]