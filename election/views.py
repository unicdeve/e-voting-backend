from datetime import datetime

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Election
from .serializers import ElectionSerializer

today = datetime.today()

# Create your views here.
class ElectionView(APIView):
    permission_classes = (IsAuthenticated, )
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    
    def get(self, request, *args, **kwargs):
        
        # Maybe optimize the code by combining both query 
        # and separating with another func
        ongoing_elections = Election.objects.all().filter(start_time__lte=today)
        upcoming_elections = Election.objects.filter(start_time__gte=today)

        ongoing_elections_qs = ElectionSerializer(ongoing_elections, many=True).data
        upcoming_elections_qs = ElectionSerializer(upcoming_elections, many=True).data

        response_data = {
          "ongoing_elections": ongoing_elections_qs,
          "upcoming_elections": upcoming_elections_qs,
        }

        return Response(response_data, status=status.HTTP_200_OK)


