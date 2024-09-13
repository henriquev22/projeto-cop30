from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/<int:product_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add/', views.add_item, name='add_item'),  # Adicionei o caminho para adicionar itens
]

