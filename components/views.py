from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from components.models import Component
from components.serializers import ComponentSerializer


@api_view(['GET', 'POST'])
def component_list(request, format=None):
    """
    List all components, or create a new component.
    """
    if request.method == 'GET':
        components = Component.objects.all()
        serializer = ComponentSerializer(components, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ComponentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def component_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        component = Component.objects.get(pk=pk)
    except Component.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ComponentSerializer(component)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ComponentSerializer(component, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        component.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
