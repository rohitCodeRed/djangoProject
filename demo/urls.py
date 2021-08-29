from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books',views.BookViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('first',views.first),
    path('another',views.Another.as_view()),
]