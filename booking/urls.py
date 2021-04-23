from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('book',views.book,name='book'),
    path('contact-us',views.contact,name='contact-us'),
    path('about-us',views.about,name='about-us'),
    path('how-it-works',views.howitworks,name='howitworks'),
    path('book-now/<str:id>',views.book_now,name='book-now'),
    path('cancel-storage/<str:id>',views.cancel_storage,name='cancel-storage'),
    path('delete-storage/<str:id>',views.delete_storage,name='delete-storage'),
    path('confirm-now-booking',views.book_confirm,name="book_confirm")

]