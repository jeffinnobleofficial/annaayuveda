from django.urls import path,include
from . import views
urlpatterns = [
    
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('products', views.productss, name='product'),
    path('appointment', views.appointment, name='appointment'),
    path('contact', views.contact, name='contact'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('register here', views.register, name='register'),
     path('book/',views.book_view,name='book'),
]
