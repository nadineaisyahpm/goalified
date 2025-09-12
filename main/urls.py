from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('json/', views.show_json, name='show_json'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path("products/", views.product_list, name="product_list"),
    path("products/<int:id>/", views.product_detail, name="product_detail"),
    path('products/add/', views.add_product, name='add_product'),
]