from .import views
from django.urls import path, include

urlpatterns = [
    # path("", views.homepage, name="homepage"),
    # path("signup/", views.UserRegistrationView, name = "signup"),
    path("postformdata/", views.postForm, name = "postformdata"),
    path("getalldata/", views.getalldata, name = "getalldata"),
]