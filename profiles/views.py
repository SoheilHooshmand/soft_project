from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny


class ProfileList(APIView):

    def get(self, request, format = None):
        lawyers = Lawyer.objects.all()
        serializer = LawyerSerializer(lawyers, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = UserSerializer(request.data)
        if serializer.is_valid():
            hash_password = make_password(request.data['password'])
            data = serializer.validated_data
            data['password'] = hash_password
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)


class ProfileDetails(APIView):
    permission_classes([IsAuthenticated])



    def get_profile(self, pk):
        try:
            return Profile.objects.get(id = pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format = None):
        profile = self.get_profile(pk)
        if isinstance(profile, Client):
            serializer = ClientSerializer(profile, many = False)
            return Response(serializer.data, status = status.HTTP_200_OK)
        elif isinstance(profile, Lawyer):
            serializer = LawyerSerializer(profile, many = False)
            return Response(serializer.data, status = status.HTTP_200_OK)


    def put(self, request, pk, format = None):
        profile = request.user.profile
        if isinstance(profile, Client):
            serializer = ClientSerializer(profile, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status = status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, fromat = None):
        profile = request.user.profile
        profile.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method == "PUT" or self.request.method == "DELETE":
            return [IsAuthenticated()]
        else:
            return [AllowAny()]













