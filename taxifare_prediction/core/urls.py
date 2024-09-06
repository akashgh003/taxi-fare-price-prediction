from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predict/', include('fare_prediction.urls')),  # Include the app URLs
]
