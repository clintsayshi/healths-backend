from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.models import Profile
from .serializers import ProfileSerializer, RegisterSerializer
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User


@api_view(['GET'])
def getRoutes(request):
    routes  = [
        {'GET': 'api/profiles', 'POST': 'api/users/token'}
    ]

    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfiles(request):
    profiles = Profile.objects.all()
    serialize = ProfileSerializer(profiles, many=True)
    return Response(serialize.data)

@api_view(['POST'])
def registerUser(request):
    data = JSONParser().parse(request)

    serialize = RegisterSerializer(data=data)

    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data)

    return Response(serialize.errors)