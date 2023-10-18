from django.test import TestCase
from django.utils import timezone  # Import timezone from django.utils
import datetime


class QuestionModelTestCase(TestCase):
    def test_was_published_recently_with_future_question(self):
        # Create a Question with a pub_date in the future
        future_time = timezone.now() + datetime.timedelta(days=1)

    def test_was_published_recently_with_past_question(self):
        # Create a Question with a pub_date in the past
        past_time = timezone.now() - datetime.timedelta(days=1)
