from django.urls import path
from . import views
from .views import login_view
from .views import signup_view

urlpatterns = [
    path('donors/', views.donor_list, name='donor_list'),
    path('add_donor/', views.add_donor, name='add_donor'),
    path('stock/', views.blood_stock, name='blood_stock'),
    path('add_request/', views.add_request, name='add_request'),
    path('requests/', views.request_list, name='request_list'),
    path('home/', views.home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
]
