from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = 'index'),
    path('login/',views.login,name="login"),
    path('homepage/',views.mainpage,name="homepage"),
    path('homepage/contactus/',views.contactus,name="contactus"),
    path('homepage/mouseclick/',views.mouseclick,name="mouseclick"),
    path('homepage/eyeblink/',views.eyeblink,name="eyeblink")
]