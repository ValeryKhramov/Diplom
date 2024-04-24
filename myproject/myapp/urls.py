from django.urls import path
from .views import index, services, contacts, inputs, account, history, montage, logout_user

urlpatterns = [
    path('', index, name='index'),
    path('services/', services, name='services'),
    path('contacts/', contacts, name='contacts'),
    path('input/', inputs, name='inputs'),
    path('logout/', logout_user, name='logout'),
    path('account/', account, name='account'),
    path('account/history/', history, name='history'),
    path('account/montage/', montage, name='montage'),
]
