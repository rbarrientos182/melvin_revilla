from django.urls import path
from .views import MemberListView

urlpatterns = [
    path('list_members/', MemberListView.as_view(), name='list_members'),
]