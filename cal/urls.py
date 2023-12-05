from django.urls import path
from django.views.generic import TemplateView
from .views import AddView, MemoView, Memo2View, Memo3View, Memo4View, Memo5View, TargetView, CalendarView, StateView, Target2View, target2  # 수정한 부분
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('add/', AddView.as_view(), name='add'),
    path('memo/', MemoView.as_view(), name='memo'),
    path('memo2/', Memo2View.as_view(), name='memo2'),
    path('memo3/', Memo3View.as_view(), name='memo3'),
    path('memo4/', Memo4View.as_view(), name='memo4'),
    path('memo5/', Memo5View.as_view(), name='memo5'),
    path('target/', TargetView.as_view(), name='target'),
    path('state/', StateView.as_view(), name='state'),
    path('target2/', Target2View.as_view(), name='target2'),
    path('target2/', target2, name='target2'),  # 수정한 부분
    path('tutorial1/', TemplateView.as_view(template_name='cal/tutorial1.html'), name='tutorial1'),  # tutorial1 추가
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
