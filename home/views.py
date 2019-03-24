from django.conf import settings
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Sauna
from home.serializers import SaunaSerializer


def home(request):
    return render(request, settings.BASE_DIR + '/aslaksmartsgateapp/dist/index.html')


@api_view(['GET', 'PUT', 'DELETE'])
def sauna_detail(request, format=None):
    try:
        sauna = Sauna.objects.get(pk=1)
    except Sauna.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SaunaSerializer(sauna)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    elif request.method == 'PUT':
        print(request.data)
        serializer = SaunaSerializer(sauna, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sauna.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)