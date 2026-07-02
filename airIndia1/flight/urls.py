from django.urls import path
from . import views
urlpatterns = [
    # Define your URL patterns here
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('bookflight', views.bookflight, name='bookflight'),
    path('bookings', views.bookings, name='bookings'),
    path('seebookings',views.seebookings,name="seebookings"),
    path('cancellings',views.cancellings,name='cancellings'),
    path('signup',views.signup, name="signup"),
    path('signin',views.signin, name="signin"),
    path('signout',views.signout, name="signout"),
    
]