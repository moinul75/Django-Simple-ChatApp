from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib import admin
from .models import Message,Room

#change the admin panel 
admin.site.site_header = "Chat Simple App"
admin.site.site_title = "My Chat App"
admin.site.site_header = "My Chat"

# Create your views here.
def home(request):
    return render(request,'index.html')

#room 
def room(request,room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    print(room_details)
    return render(request, 'room.html',{
        'username':username,
        'room':room,
        'room_details': room_details
    } )
    


#checkout room exits or not create a room 
def checkout(request):
    username = request.POST['username']
    room = request.POST['room_name']
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
    
#send messages save 
def send(request):
    
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    
    new_message = Message.objects.create(value=message,user=username,room =room_id)
    new_message.save()
    return HttpResponse("Message Sent Successfully!!")  

def getMessages(request,room):
    room_details = Room.objects.get(name=room) 
    messages = Message.objects.filter(room__icontains=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
    
    


