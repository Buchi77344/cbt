# authentication.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import UserID

class IDBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user_id = UserID.objects.get(generated_id=username)
            return user_id.user
        except UserID.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
