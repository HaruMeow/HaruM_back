from django.urls import path
from .views import AddView, MemoView, TargetView, CalendarView, StateView

urlpatterns = [
    path('', CalendarView.as_view(), name='calendar'),
    path('add/', AddView.as_view(), name='add'),
    path('memo/', MemoView.as_view(), name='memo'),
    path('target/', TargetView.as_view(), name='target'),
    path('state/', StateView.as_view(), name='state'),
    path('calendar/', CalendarView.as_view(), name='calendar'),

]