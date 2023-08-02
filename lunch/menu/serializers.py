from rest_framework import serializers
from .models import MenuItem, Menu
from restaurant.models import Restaurant
from rest_framework import exceptions

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, write_only=False)  # Changed write_only to False for items field
    restaurant_name = serializers.CharField(write_only=True)

    class Meta:
        model = Menu
        fields = ['name', 'date', 'items', 'restaurant_name']

    def create(self, validated_data):
        restaurant_name = validated_data.pop('restaurant_name')
        items_data = validated_data.pop('items')
        menu_items = []
        try:
            restaurant = Restaurant.objects.get(name=restaurant_name)
        except Restaurant.DoesNotExist as ex:
            raise exceptions.NotFound("No such restaurant")
        # Create the menu with the restaurant
        menu = Menu.objects.create(restaurant=restaurant, **validated_data)

        # Create menu items
        for item_data in items_data:
            menu_item = MenuItem.objects.create(**item_data)  # Use the create method here
            menu_items.append(menu_item)

        # Set the menu items to the menu instance (many-to-many relationship)
        menu.items.set(menu_items)
        restaurant.menus.add(menu)

        return menu


