import os
from trydjango import settings
from django.test import TestCase

class Trydjangotest(TestCase):
    def test_first(self):
        SECRET_KEY = os.environ.get('SECRET_KEY')

        self.assertNotEqual(SECRET_KEY,12)
        msg = "this is the error "
        try:
            do_somthing
        except Exception:
            self.fail(msg)