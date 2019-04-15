from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from board import views
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list),
    path('write', views.write),
    path('insert', views.insert),
    path('download', views.download),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#디버그 툴바 관련 url mapping
if settings.DEBUG: #settings.py의 DEBUG 변수 설정
    import debug_toolbar #debug_toolbar 기능을 가져옴
    #debug_toolbar의 url 패턴 정의
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]