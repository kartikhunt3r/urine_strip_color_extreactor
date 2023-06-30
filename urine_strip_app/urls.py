from django.urls import path
from .views import upload_strip

urlpatterns = [
    path('', upload_strip, name='upload_strip'),
]
