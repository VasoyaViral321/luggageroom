from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('login',views.user_login,name='user_login'),
    path('login1',views.Admin_login,name='Admin_login'),
    path('signup',views.user_signup,name='user_signup'),
    path('signup1',views.Admin_signup,name='Admin_signup'),
    path('dashboard/',include('customer.urls')),
    path('dashboard1/',include('room_admin.urls')),
    path('add-storage/',include('room_admin.urls')),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='login/password_reset.html',
             subject_template_name='login/password_reset_subject.txt',
             email_template_name='login/password_reset_email.html',
             success_url='login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='login/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='login/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='login/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('password-reset1/',
         auth_views.PasswordResetView.as_view(
             template_name='login/password_reset.html',
             subject_template_name='login/password_reset_subject.txt',
             email_template_name='login/password_reset_email.html',
         ),
         name='password_reset'),
    path('done1/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='login/password_reset_done.html'
             
         ),
         
         name='password_reset_done'),
    path('password-reset-confirm1/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='login/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete1/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='login/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]