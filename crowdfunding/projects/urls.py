from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
]
<<<<<<< HEAD
urlpatterns = format_suffix_patterns(urlpatterns)
=======
urlpatterns = format_suffix_patterns(urlpatterns)
>>>>>>> modelrelationstest
