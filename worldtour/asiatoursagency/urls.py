from django.urls import path
from . import views # from current directory import views file

# Define a list of url patterns that user want to navigate
urlpatterns = [
    path('',views.index)
]