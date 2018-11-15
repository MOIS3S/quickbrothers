from django.urls import path
from .views import ProjectListView, ProjectDetailView, contact


core_patterns = ([
    path('', ProjectListView.as_view(), name="home"),
    path('<int:pk>/<slug:slug>/', ProjectDetailView.as_view(), name="detail"),
    path('contact', contact, name="contact"),
], 'core')