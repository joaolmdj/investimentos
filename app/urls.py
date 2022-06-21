from django.urls import path

from . import views

urlpatterns = [
    path('', views.proprietarios),
    path('investimento/<id>', views.investimento, name='list_investimento'),
    path('investimento/<id>/create', views.create_investimento, name='create_investimento'),
    path('investimento/<id>/view', views.view_investimento, name='view_investimento'),
    path('investimento/<id>/update', views.update_investimento, name='update_investimento'),
    path('investimento/<id>/delete', views.delete_investimento, name='delete_investimento'),
]