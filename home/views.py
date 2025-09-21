from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import MenuCategory
from .serializers import MenuCategorySerializer

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = [AllowAny]

@api_view(['GET'])
@permission_classes([AllowAny])
def MenuCategory_func_view(request):
    categories = MenuCategory.all()
    serializer = MenuCategorySerializer(categories,many=True)
    return Response(serializer.data)