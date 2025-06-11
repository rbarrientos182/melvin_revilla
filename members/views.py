from django.shortcuts import render
from django.views import generic
from .models import Member

class MemberListView(generic.ListView):
    model = Member
    context_object_name = 'members'
    template_name = "members/list_members.html"
