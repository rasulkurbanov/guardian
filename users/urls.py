from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('', views.profiles, name="profiles"),
    path('profile/<uuid:profile_id>', views.userProfile, name='user-profile'),
    path('account/', views.userAccount, name="account"),
    path('edit-account/', views.editAccount, name="edit-account"),
    path('create-skill/', views.createSkill, name="create-skill"),
    path('update-skill/<uuid:skill_id>', views.updateSkill, name='update-skill'),
    path('delete-skill/<uuid:skill_id>', views.updateSkill, name='delete-skill')

]
