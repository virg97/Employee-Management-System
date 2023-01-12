from django.urls import path

from angajati import views

app_name = 'angajati'

urlpatterns = [

    path('', views.AngajatiView.as_view(), name='lista_nume'),
    path('adaugare/', views.CreateAngajatiView.as_view(), name='adaugare'),
    path('<int:pk>/update/', views.UpdateAngajatiView.as_view(), name='modificare'),
    path('delete/<int:pk>/', views.delete_angajati, name='delete'),
    path('activate/<int:pk>/', views.activate_angajati, name='activate'),

]
