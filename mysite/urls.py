from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('cal/', include('cal.urls')),
    path('join/', TemplateView.as_view(template_name='index.html'), name='join'),  # 이 부분을 추가
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]