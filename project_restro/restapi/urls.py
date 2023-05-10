from django.urls import path
from .views import CategoryApiView, MenuApiView, CategoryApiIdView

urlpatterns = [
    path('category/', CategoryApiView.as_view()),
    path('category/<int:id>/', CategoryApiIdView.as_view()),
    path('menu/', MenuApiView.as_view())
]