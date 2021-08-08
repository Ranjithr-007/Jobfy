from django.shortcuts import render,redirect
import uuid
from message.models import *
from account.models import *
import operator
from django.dispatch.dispatcher import receiver

def chat(request):
    if request.user.is_authenticated:
        chats = []
        chats_user1 = OneToOne.objects.filter(user1=request.user)
        chats_user2 = OneToOne.objects.filter(user2=request.user)
        for x in chats_user1:
            chats.append(x)
        for x in chats_user2:
            chats.append(x)
        exist = True
        if len(chats) == 0:
            exist = False
        context = {
            'chats':chats,
            'exist':exist
        }
        return render(request, 'chat/chat.html', context)
    else:
        return redirect('account:user_logIn')

def chat_room(request, id):
    if request.user.is_authenticated:
        receiver = User.objects.get(id=id)
        if OneToOne.objects.filter(user1=request.user, user2=receiver).exists():
            onetoone = OneToOne.objects.get(user1=request.user, user2=receiver)
            room_name = onetoone.room_name
            messages = Messages.objects.filter(onetoone=onetoone)
            context ={
                'receiver':receiver,
                'room_name':room_name,
                'messages':messages,
                'onetoone':onetoone
            }
        elif OneToOne.objects.filter(user2=request.user, user1=receiver).exists():
            onetoone = OneToOne.objects.get(user2= request.user, user1= receiver)
            room_name = onetoone.room_name
            messages = Messages.objects.filter(onetoone=onetoone)
            context = {
                'receiver':receiver,
                'room_name':room_name,
                'messages':messages,
                'onetoone':onetoone
            }
        else:
            room_name = uuid.uuid1()
            context = {
                'receiver':receiver,
                'room_name': room_name,
                'messages': '0'
            }
        return render(request, 'chat/chat_room.html', context)
    else:
        return redirect('account:user_logIn')