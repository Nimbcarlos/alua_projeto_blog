from django.urls import path
from blog.views import (CategoryListView, CreatedByListView, PostListView,
                        PageDetailView, PostDetailView, SearchListView, TagListView)
app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('page/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path(
        'created_by/<int:author_pk>/',
        CreatedByListView.as_view(),
        name='created_by'
    ),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post'),
    path('tag/<slug:slug>/', TagListView.as_view(), name='tag'),
    path('search/', SearchListView.as_view(), name='search'),
]
