from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Profile
from .serializers import ProfileSerializer


@api_view(['GET'])
def getRoutes(request):
    routes  = [
        {'GET': 'api/projects', 'POST': 'api/users/token'}
    ]

    return Response(routes)

@api_view(['GET'])
def getProfiles(request):
    profiles = Profile.objects.all()
    serialize = ProfileSerializer(profiles, many=True)
    return Response(serialize.data)