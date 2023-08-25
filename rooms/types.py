import strawberry
from strawberry import auto
from . import models


@strawberry.django.type(models.Room)
class RoomType:
    id: auto # auto 로 지정하면 타입을 자동으로 추론합니다.
    name: auto
    kind: auto