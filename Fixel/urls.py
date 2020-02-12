from django.contrib import admin
from django.conf.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from dashboard import data
from modules import convert
import base64

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]




#image =
#convert.conv64(image)
#urlpatterns = format_suffix_patterns(urlpatterns)
