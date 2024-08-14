from . import views
from django.urls import path
app_name ="admins"
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('signup',views.signup,name= "signup")
]
