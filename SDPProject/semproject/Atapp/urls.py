from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('home/', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path('services/', views.services,name="services"),
    path('team/', views.team,name="team"),
    path('gallery/', views.gallery,name="gallery"),
    path('faqs/', views.faqs,name="faqs"),
    path('terms/', views.terms,name="terms"),
    path('signin/', views.signin,name="signin"),
    path('signup/', views.signup,name="signup"),
    path('signout/', views.signout,name="signout"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('thanks/', views.thanks,name="thanks"),
]

