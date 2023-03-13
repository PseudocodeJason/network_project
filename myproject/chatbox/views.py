from django.shortcuts import render

from .models import Chatmessage,User,Response


def index(request):
    return render(request, "chatbox/base.html")


def chat_history(request):
    chats = Chatmessage.objects.all()
    chats_list = []
    for chat in chats:
        chats_list.append({"chat": chat})

    context = {
        "chats_list": chats_list
    }
    return render(request, "chatbox/chat_history.html", context)



def user_list(request):
    users = User.objects.all()
    users_list = []
    for user in users:
        users_list.append({"user": user})

    context = {
        "users_list": users_list
    }
    return render(request, "chatbox/user_list.html", context)

def response_history(request):
    responses = Response.objects.all()
    responses_list = []
    for response in responses:
        responses_list.append({"response": response})

    context = {
        "responses_list": responses_list
    }
    return render(request, "chatbox/response_history.html", context)