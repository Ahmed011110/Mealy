from django.contrib import admin
from django.urls import path, include
from mealy import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register("g", views.viewsets_guest)
router.register("m", views.viewsets_movie)
router.register("re", views.viewsets_reservation)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("1", views.no_rest_no_model),
    path("2", views.no_rest_from_model),
    path("3.1", views.FBV_List),
    path("3.2/<int:pk>/", views.FBV_pk),
    path("4.1", views.CBV_List.as_view()),
    path("4.2/<int:pk>", views.CBV_pk.as_view()),
    path("5.1", views.mixins_list.as_view()),
    path("5.2/<int:pk>", views.mixins_pk.as_view()),
    path("6.1", views.Generics_List.as_view()),
    path("6.2/<int:pk>", views.Generics_pk.as_view()),
    path("7", include(router.urls)),
    path("8", views.find_movie),
    path("9", views.new_reservation),
    path("10", include("rest_framework.urls")),
    path("11", obtain_auth_token),
    path("12/<int:pk>", views.post_pk.as_view()),
]
