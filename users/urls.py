from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', views.registerUser, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('reset/password/', auth_views.PasswordResetView.as_view(template_name="users/reset/reset.html"), name="reset_password"),
    path('reset/password/sent/', auth_views.PasswordResetDoneView.as_view(template_name="users/reset/reset_sent.html"), name="password_reset_done"),
    path('password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/reset/set_password.html"), name="password_reset_confirm"),
    path('reset/password/done', auth_views.PasswordResetCompleteView.as_view(template_name="users/reset/reset_complete.html"), name="password_reset_complete"),
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>', views.userProfile, name="user-profile"),
    path('account/', views.userAccount, name="account"),
    path('edit-account/', views.editAccount, name="edit-account"),
    path('create-skill/', views.createSkill, name="create-skill"),
    path('edit-skill/<str:pk>', views.editSkill, name="edit-skill"),
    path('delete-skill/<str:pk>', views.deleteSkill, name="delete-skill"),
    
    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>', views.messagePage, name="message"),
    path('send-message/<str:pk>/', views.sendMessage, name="send-message")
]
