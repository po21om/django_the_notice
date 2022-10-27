"""the_notice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from the_notice import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    # pusta ścieżka jak dałbym np a/ to byłoby np a/admin
    path("", include("accounts.urls")),
    path("", include("viewer.urls")),
    #
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^viewer/static/viewer/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]
# handlery nające obsłużyć - jak debugv w settings - tRue to nie zadziałają
handler404 = 'viewer.views.error_404'
handler500 = 'viewer.views.error_500'
