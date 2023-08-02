from rest_framework import viewsets, status
from .models import MenuItem, Menu
from .serializers import MenuItemSerializer, MenuSerializer
from employee.permissions import CanCreateRestaurant
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated, CanCreateRestaurant]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def create_menu_with_items(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            menu = serializer.create_menu(serializer.validated_data)
            return Response(self.serializer_class(menu).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put', 'patch'])
    def update_menu_with_items(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['delete'])
    def delete_menu(self, request, pk=None):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Menu deleted successfully."}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        menu = queryset.filter(pk=pk).first()
        if menu:
            serializer = self.serializer_class(menu)
            return Response(serializer.data)
        return Response({"error": "Menu not found."}, status=status.HTTP_404_NOT_FOUND)
