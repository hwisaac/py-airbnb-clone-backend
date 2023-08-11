from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHello(request):
    return HttpResponse("hello")

def see_one_room(request, room_id):
    return HttpResponse(f"see room with id : {room_id}")