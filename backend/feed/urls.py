from django.urls import path
from .views import PostAPIList, PostDetailAPI, CommentAPIList, CommentDetailAPI


urlpatterns = [
    path('post/', PostAPIList.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailAPI.as_view(), name='post'),
    path('comment/', CommentAPIList.as_view(), name='comment_list'),
    path('comment/<int:pk>', CommentDetailAPI.as_view(), name='coment'),
]