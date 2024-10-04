from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
import smash_db.models


class SettingsBackend(BaseBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """

    def authenticate(self, request, tag=None):
        try:
            user = smash_db.models.My_User.objects.get(tag=tag)
            return user
        except smash_db.models.My_User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return smash_db.models.My_User.objects.get(pk=user_id)
        except smash_db.models.My_User.DoesNotExist:
            return None