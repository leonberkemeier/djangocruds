from django.urls import path
from .import views



urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test, name="test"),
    path("renderrndtpl", views.renderrndtpl, name="renderrndtpl"),
    path("rendernexttpl", views.rendernexttpl, name="rendernexttpl"),
    # path("renderprevtpl", views.renderprevtpl, name="renderprevtpl"),

]