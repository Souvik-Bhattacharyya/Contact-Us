from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('our_projects/', views.project_view, name='our_projects'),
    path('our_projects/<int:category>/',
         views.project_view, name='our_projects_category'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('about_us/', views.about_view, name='about'),
    path('contact_us/', views.contact_view, name='contact'),
    path('details/<int:prj_id>/', views.details_view, name='details'),
]
