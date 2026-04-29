from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.landing_page, name='landing_page'),
    path('about/', views.about_us, name='about_us'),
    path('services/', views.services_overview, name='services_overview'),
    path('projects/', views.projects_catalog, name='projects_catalog'),
    path('projects/villa-nordica/', views.project_detail_villa_nordica, name='project_detail_villa_nordica'),
    path('projects/comparison/', views.project_comparison, name='project_comparison'),
    path('projects/zenith/', views.portfolio_project_zenith, name='portfolio_project_zenith'),
    path('portfolio/map/', views.portfolio_map_view, name='portfolio_map_view'),
    path('design/individual/', views.individual_design, name='individual_design'),
    path('financing/mortgage/', views.mortgage_financing, name='mortgage_financing'),
    path('learn/house-area/', views.educational_house_area_explained, name='educational_house_area_explained'),
    path('careers/', views.careers, name='careers'),
    path('contact/', views.contact_us, name='contact_us'),
]
