from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('check/', views.LessonListAPIView.as_view(), name='check'),
    path('order/', views.AllProductsListAPIView.as_view(), name='order'),
    path('new_user/', views.RenderNewAccessAPIView.as_view(), name='work,pls)')
]
