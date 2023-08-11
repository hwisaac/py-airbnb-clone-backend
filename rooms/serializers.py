from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomDetailSerializer(ModelSerializer):

    owner = TinyUserSerializer() # owner 를 가져올때 TinyUserSerializer 를 이용하라
    amenities = AmenitySerializer(many=True)
    category = CategorySerializer()
    class Meta:
        model = Room
        fields = "__all__"
        depth = 1


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
        )