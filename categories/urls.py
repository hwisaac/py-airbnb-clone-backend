from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.CategoryViewSet.as_view(
            {
                "get": "list", # get 요청이 오면 list라는 메소드의 코드 실행
                "post": "create", # post 요청이오면 create메소드 실행
            }
        ),
    ),
    path(
        "<int:pk>",
        views.CategoryViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]