from django.urls import path
from .views import ProductView,CreateView,clean,main
app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('list/', ProductView.as_view()),
    path('create/',CreateView.as_view()),
    path('clean/',clean),
    path('',main)
]