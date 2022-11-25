from django.contrib import admin
from django.urls import path
from leave import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken
router=DefaultRouter()
router.register("leave",views.LeaveView,basename="lev")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', ObtainAuthToken.as_view()),

              ]+router.urls