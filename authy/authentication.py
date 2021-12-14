from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()


class NINBackend(object):
   def authenticate(self, request, nin=None):
      try:
         return UserModel.objects.get(nin=nin)
      except UserModel.DoesNotExist:
         pass

      return None


   def get_user(self, pk):
      try:
         return UserModel.objects.get(pk=pk)
      except UserModel.DoesNotExist:
         return None
