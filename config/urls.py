from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/rooms/", include("rooms.urls")),
    path("api/v1/categories/", include("categories.urls")),
    path("api/v1/experiences/", include("experiences.urls")),
    path("api/v1/medias/", include("medias.urls")),
    path("api/v1/wishlists", include("wishlists.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # "user-uploads/" (URL과), 정적파일이 저장된 폴더명 "uploads" 를 인자로 넣어줍니다.
