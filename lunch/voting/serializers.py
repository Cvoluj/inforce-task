from rest_framework import serializers
from .models import MenuVote

class MenuVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuVote
        fields = '__all__'