from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home(request):
    return redirect('my_tasks')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasks.urls")),
]

