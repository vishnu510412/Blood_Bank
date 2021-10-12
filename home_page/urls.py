from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('userdata/',views.userdata, name='userdata'),
    path('lists/',views.index,name='home'),
    path('signup/',views.signup,name='signup'),
    path('lists/logout/',views.login,name='logout'),
    path('logout/',views.login,name='logout'),
    path('login/',views.login,name='login')
]