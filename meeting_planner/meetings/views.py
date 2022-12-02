from django.shortcuts import render, get_object_or_404

from .models import Meeting


def detail(request, room_id):
    meeting = get_object_or_404(Meeting, pk=room_id)
    return render(request, "meetings/detail.html", {"meeting": meeting})
