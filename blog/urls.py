from django.urls import path
from .views import PostListView, post_details

app_name = 'blog'

urlpatterns = [
    path("", PostListView.as_view(), name="list_view"),
    path("<int:year>/<int:month>/<int:day>/<slug:slug>", post_details, name="post_detail")
]