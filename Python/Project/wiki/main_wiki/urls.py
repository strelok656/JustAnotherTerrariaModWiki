from django.urls import path
from . import views

app_name = 'main_wiki'

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('wiki-pages/<str:url_title>/', views.wiki_page, name='wiki_page'),
    path('registration/', views.reg, name='reg'),
    path('personalAccount/', views.acc, name='personalAccount'),
    path('logout/', views.logout_view, name='logout'),
]
