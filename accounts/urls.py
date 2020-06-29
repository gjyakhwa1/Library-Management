from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('updateuser/<int:id>', views.update_user, name="update_user"),
    path('confirmdeleteuser/<int:id>', views.confirm_delete_user, name="confirm_deleteuser"),
    path('deleteuser/<int:id>', views.delete_user, name="deleteuser")
]
