from django.urls import path


from . import views


app_name = 'userprofile'


urlpatterns = [
    path('myaccount/', views.myaccount, name='myaccount'),
    path('signup/<str:role>/', views.signup, name='signup'),
]