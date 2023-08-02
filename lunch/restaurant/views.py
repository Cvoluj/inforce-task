from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Restaurant
from .serializers import RestaurantSerializer
from employee.permissions import CanCreateRestaurant

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated, CanCreateRestaurant]

    def list(self, request):
        """
        Get a list of all restaurants.
        URL: /api/restaurants/
        Command: GET /api/restaurants/
        """
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new restaurant.
        URL: /api/restaurants/
        Command: POST /api/restaurants/ with JSON data in the request body. as 
        {
        "name": "Delicious Restaurant",
        "address": "123 Main Street"
        }
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        """
        Get a specific restaurant by its primary key.
        URL: /api/restaurants/{restaurant_id}/
        Command: GET /api/restaurants/{restaurant_id}/
        """
        queryset = self.get_queryset()
        restaurant = queryset.filter(pk=pk).first()
        if restaurant:
            serializer = self.serializer_class(restaurant)
            return Response(serializer.data)
        return Response({"error": "Restaurant not found."}, status=404)

    def update(self, request, *args, **kwargs):
        """
        Update a specific restaurant by its primary key.
        URL: /api/restaurants/{restaurant_id}/
        Command: PUT /api/restaurants/{restaurant_id}/ or PATCH /api/restaurants/{restaurant_id}/ with JSON data in the request body.
        {
        "name": "Delicious Restaurant",
        "address": "123 Main Street"
        }
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def destroy(self, request, pk=None):
        """
        Delete restraunt
        URL: /api/restaurants/{restaurant_id}/
        Command: DELETE /api/restaurants/{restaurant_id}/
        """
        queryset = self.get_queryset()
        restaurant = queryset.filter(pk=pk).first()
        if restaurant:
            restaurant.delete()
            return Response({"message": "Restaurant deleted successfully."})
        return Response({"error": "Restaurant not found."}, status=404)