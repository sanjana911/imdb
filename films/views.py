from django.shortcuts import render,get_object_or_404


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from films.models import Movie
from films.serializer import MovieSerializer

# Create your views here.


class MovieListCreateView(APIView):

    def get(self, request):

        instance = Movie.objects.all()

        serializer_instance = MovieSerializer(instance, many = True)

        return Response(serializer_instance.data, status= status.HTTP_200_OK)

    def post(self, request):

        form_data = request.data

        serializer_instance = MovieSerializer(data = form_data)

        if serializer_instance.is_valid():

            instance = Movie.objects.create(**form_data)

            serializer_instance = MovieSerializer(instance)

            return Response(serializer_instance.data, status= status.HTTP_201_CREATED)

        else:

            return Response(serializer_instance.errors, status= status.HTTP_400_BAD_REQUEST)


class MovieRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk = None):

        instance = get_object_or_404(Movie, id = pk)

        serializer_instance = MovieSerializer(instance)

        return Response(serializer_instance.data, status= status.HTTP_200_OK)

    def put(self, request, pk = None):

        instance = get_object_or_404(Movie, id = pk)

        form_data = request.data

        serializer_instance = MovieSerializer(data = form_data)

        if serializer_instance.is_valid():

            Movie.objects.filter(id=pk).update(**form_data)

            return Response(form_data,status= status.HTTP_202_ACCEPTED)

        else:

            return Response(serializer_instance.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk = None):

        instance = get_object_or_404(Movie, id = pk)

        instance.delete()

        return Response({"message":"deleted.."}, status= status.HTTP_200_OK)

