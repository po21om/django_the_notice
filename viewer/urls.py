from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import NoticeList, NoticeDetail, NoticeCreate, NoticeUpdate, NoticeDelete, NoticeOwnList

urlpatterns = [
    path("", NoticeList.as_view(), name="notices"),
    path("my/", NoticeOwnList.as_view(), name="own_notices"),
    path("notice/<int:pk>", NoticeDetail.as_view(), name="notice"),
    path("notice-create/", NoticeCreate.as_view(), name="notice-create"),
    path("notice-update/<int:pk>", NoticeUpdate.as_view(), name="notice-update"),
    path("notice-delete/<int:pk>", NoticeDelete.as_view(), name="notice-delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
