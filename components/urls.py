from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from components import views

urlpatterns = [
    path('components/', views.component_list),
    path('components/<int:pk>', views.component_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)