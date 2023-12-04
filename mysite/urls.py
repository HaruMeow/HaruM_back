# 프로젝트의 urls.py

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('cal/', include('cal.urls')),
    path('join/', TemplateView.as_view(template_name='index.html'), name='index'),  # 'join'을 'index'로 변경
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
