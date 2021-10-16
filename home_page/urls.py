from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.user_login, name='login'),
    path('userdata/',views.userdata, name='userdata'),
    path('lists/',views.index,name='home'),
    path('signup/',views.signup,name='signup'),
    path('lists/logout/',views.user_login,name='logout'),
    path('logout/',views.user_logout,name='logout'),
    path('login/',views.user_login,name='login')
]