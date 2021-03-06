from django.urls import path
from .views import *

urlpatterns = [
    #path('', NewsList.as_view(), name='index'),
    path('', index, name='index'),
    #path('<slug:slug>/', NewsDetail.as_view(), name='news_detail'),
    path('menu/', menu, name='menu'),
    path("menu/<slug>", menu, name='menu_category'),
    path("menu/<slug:slug>", menu_detail, name='menu_detail'),
    path('about/', about, name='about'),
    #path('news/', news, name='news'),
    path('special_menu/', special_menu, name='special_menu'),
    path('contact/', contact, name='contact'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/',  LogOutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name="register"),
    path("user/", userpage, name="userpage"),
    path('profile/', profile, name="profile"),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

]