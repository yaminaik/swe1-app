from django.test import TestCase
from .models import Question
from django.utils import timezone  # Import timezone from django.utils
import datetime


class QuestionModelTestCase(TestCase):
    def test_was_published_recently_with_future_question(self):
        # Create a Question with a pub_date in the future
        future_time = timezone.now() + datetime.timedelta(days=1)
        future_question = Question(pub_date=future_time)

    def test_was_published_recently_with_past_question(self):
        """
        Test the behavior of the was_published_recently method for past questions.
        """
        # Create a Question with a pub_date in the past
        past_time = timezone.now() - datetime.timedelta(days=1)
        past_question = Question(pub_date=past_time)
