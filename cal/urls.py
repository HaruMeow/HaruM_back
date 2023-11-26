from django.urls import path
from .views import AddView, MemoView, TargetView, CalendarView, StateView
from .views import Target2View
from . import views

urlpatterns = [
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('add/', AddView.as_view(), name='add'),
    path('memo/', MemoView.as_view(), name='memo'),
    path('target/', TargetView.as_view(), name='target'),
    path('state/', StateView.as_view(), name='state'),
    path('target2/', Target2View.as_view(), name='target2'),
    path('target2/', views.target2, name='target2'),
]
