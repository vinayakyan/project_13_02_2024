from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employee_app.views import EmployeeViewSet

router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employees')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),    
]
