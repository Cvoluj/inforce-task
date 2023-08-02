from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import MenuVote
from menu.models import Menu
from menu.serializers import MenuSerializer
from .serializers import MenuVoteSerializer
from datetime import date

class MenuVoteView(CreateAPIView):
    serializer_class = MenuVoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return MenuVote.objects.filter(employee=user)

class TodaysMenusAPIView(CreateAPIView):

    serializer_class = MenuVoteSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = date.today()
        menus = Menu.objects.filter(date=today)
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)