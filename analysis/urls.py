from django.urls import path
from . import views


urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("summary", views.summary.as_view(), name="summary"),
]
