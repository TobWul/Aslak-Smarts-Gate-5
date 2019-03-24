from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from home import views

urlpatterns = [
    path('sauna/', views.sauna_detail, name="sauna"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
