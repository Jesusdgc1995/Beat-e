from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post, Comment


class FeedTest(TestCase):
    @classmethod
    def setUp(cls):
        # Create user
        testuser1 = User.objects.create_user(username="testuser1", password="123546")
        testuser1.save()

        testuser2 = User.objects.create_user(username="testuser2", password="123546")
        testuser2.save()

        # Create a feed post
        test_post = Post.objects.create(user=testuser1, content="Test feed post")
        test_post.save()

        # Add like to post
        test_like = Post.objects.get(id=1)
        test_like.like()
        test_like.save()

        # Create comment
        test_comment = Comment.objects.create(user=testuser2, post = test_post, content="Excelente test")
        test_comment.save()
    
    def test_feed_post(self):
        post = Post.objects.get(id=1)
        comment = Comment.objects.get(id=1)

        user = f'{post.user}'
        content = f'{post.content}'
        numLikes = f'{post.numLikes}'

        commentUser = f'{comment.user}'
        commentContent = f'{comment.content}'

        self.assertEqual(user, 'testuser1')
        self.assertEqual(content, 'Test feed post')
        self.assertEqual(numLikes, '1')
        self.assertEqual(commentUser, 'testuser2')
        self.assertEqual(commentContent, 'Excelente test')
