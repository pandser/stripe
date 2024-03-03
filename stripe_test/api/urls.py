from django.urls import path

from . import views


app_name = 'api'

urlpatterns = [
    path('buy/<int:pk>/', view=views.buy, name='buy'),
    path('success/', views.SuccessView.as_view()),
    path('cancel/', views.CancelView.as_view()),
    path('item/<int:pk>/', view=views.item, name='item'),
]
