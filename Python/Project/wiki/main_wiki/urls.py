from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('wiki-pages/Absorber/', views.absorber, name='absorber'),
    path('wiki-pages/AshSlicer/', views.ash_slicer, name='ash_slicer'),
    path('wiki-pages/CoolStar/', views.cool_star, name='cool_star'),
    path('wiki-pages/BloomingCrimtane/', views.blooming_crimtane, name='blooming_crimtane'),
    path('registration/', views.reg, name='reg'),
    path('personalAccount/', views.acc, name='personalAccount'),
    path('logout/', views.logout_view, name='logout'),
]
