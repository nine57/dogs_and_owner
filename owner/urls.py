from django.urls import path

from owner.views import OwnersView, DogsView

urlpatterns = [
    path('/owner', OwnersView.as_view()),
    path('/dog', DogsView.as_view()),
    
]