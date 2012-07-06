from django.shortcuts import render_to_response
from django.contrib.auth.models import User

def index(request):
    users = User.objects.all()
    user_data = {}

    for user in users:
        user_data[user.pk] = {
            'username': user.username,
            'image': user.gifs.latest_gif(),
        }

    return render_to_response('gifs/index.html', { 'users': user_data })
