from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path("", views.RequestsCatcherView.as_view()),
]
