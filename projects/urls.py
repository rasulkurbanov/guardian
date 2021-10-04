from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('<uuid:project_id>', views.project, name='project'),
    path('new-project', views.createProject, name='new-project'),
    path('update-project/<uuid:project_id>',
         views.updateProject, name='update-project'),
    path('delete-project/<uuid:project_id>',
         views.deleteProject, name='delete-project')
]
