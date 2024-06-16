from django.shortcuts import render, redirect
from tonitalk_app.models import ChatRoom, ChatMessages
from django.http import HttpResponse,JsonResponse
# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def get_room(request, room):
    user_name = request.GET.get('username')
    room_details = ChatRoom.objects.get(room_name=room)
    context = {
        'user_name':user_name,
        'room_name':room,
        'room_details':room_details
    }
    return render(request, 'chatroom.html', context)

def check_room(request):
    chat_room = request.POST['room_name']
    user_name = request.POST['username']

    if ChatRoom.objects.filter(room_name=chat_room).exists():
        return redirect('/'+chat_room+'/?username='+user_name)
    else:
        new_room = ChatRoom.objects.create(room_name=chat_room)
        new_room.save()
        return redirect('/'+chat_room+'/?username='+user_name)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = ChatMessages.objects.create(user_message=message, sender=username, user_room=room_id)
    new_message.save()
    return HttpResponse('message sent successful')

def get_messages(request, room):
    room_details = ChatRoom.objects.get(room_name=room)
    messages = ChatMessages.objects.filter(user_room=room_details.id)
    return JsonResponse({ 'messages' : list(messages.values()) })