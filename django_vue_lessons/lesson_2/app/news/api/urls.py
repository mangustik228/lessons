from django.urls import path
# from news.api.views import article_list_create_api_view, article_detail_api_view

# urlpatterns = [
#     path("articles/", article_list_create_api_view, name="article-list"),
#     path("articles/<int:pk>", article_detail_api_view, name="article-detail"),
# ]

import news.api.views as V


urlpatterns = [
    path("articles/",
         V.ArticleListAPIView.as_view(),
         name="article-list"),

    path("journalists/",
         V.JournalistListApiView.as_view(),
         name="journalist-list"),

    path("articles/<int:pk>",
         V.ArticleDetailAPIView.as_view(),
         name="article-detail"),
]
