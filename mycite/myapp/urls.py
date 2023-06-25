from django.urls import path 
from .import views

app_name = 'myapp'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
	path('create/', views.ListCreateview.as_view(),name='create'),
	path('update/<pk>', views.Updateview.as_view(), name='update'),
	path('delete/<pk>', views.DeleteStudentView.as_view(), name='delete'),
	path('paid/', views.PayListview.as_view(), name='paid'),
	path('unpaid/', views.PaidListview.as_view(), name='unpaid'),
	path('searchis/', views.search_base, name='searchis'),
    
    
    
]

    