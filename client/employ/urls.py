from django.contrib import admin
from django.urls import path
from employ import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken
router=DefaultRouter()
router.register("employ",views.EmployeView,basename="emp")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', ObtainAuthToken.as_view()),

              ]+router.urls