from django.urls import path
from .views import all_units, single_unit, new_unit, unit_edit, unit_delete, unit_list, unit_update, unit_detail



app_name='units'

urlpatterns = [
    path('' , all_units , name='all_units_list'),
    path('new/' , new_unit , name='new_unit'),
    path('<str:slug>',single_unit,name='unit_detail'),
    path('<str:slug>/edit',unit_edit,name='unit_edit'),
    path('<str:slug>/delete',unit_delete,name='unit_delete'),

    #class based views
    path('cbv/<str:slug>',unit_detail.as_view(), name='cbv_detail'),
    path('cbv/new',unit_update.as_view()),
    path('cbv/<str:slug>/edit',unit_update.as_view()),
    path('cbv/',unit_list.as_view()),
]