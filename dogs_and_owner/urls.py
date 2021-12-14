from django.urls import path, include

urlpatterns = [
    path('dogs_and_owner', include('owner.urls')),
    
]