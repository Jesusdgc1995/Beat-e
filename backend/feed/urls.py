from django.urls import path
from .views import PostAPIList, PostDetailAPI, CommentAPIList, CommentDetailAPI


urlpatterns = [
    path('post/', PostAPIList.as_view()),
    path('post/<int:pk>', PostDetailAPI.as_view()),
    path('comment/', CommentAPIList.as_view()),
    path('comment/<int:pk>', CommentDetailAPI.as_view()),
]