from django.urls import path
import ebooks.api.views as V


urlpatterns = [
    path("ebooks/", V.EbookListCreateApiView.as_view(), name="ebook-list")
]
