from django.urls import path
from .views import all_units, single_unit, new_unit, unit_edit, unit_delete



app_name='units'

urlpatterns = [
    path('' , all_units , name='all_units_list'),
    path('new/' , new_unit , name='new_unit'),
    path('<str:slug>',single_unit,name='unit_detail'),
    path('<str:slug>/edit',unit_edit,name='unit_edit'),
    path('<str:slug>/delete',unit_delete,name='unit_delete')
]