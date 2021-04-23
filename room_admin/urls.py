from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name="manager_dashboard"),
    path('new/',views.add_storage,name="add_storage"),
    path('update/<str:storage_location>/',views.update_storage,name="update_storage"),

]
