from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import Http404

def index(request):
    users = User.objects.all()
    user_data = {}

    for user in users:
        user_data[user.pk] = {
            'username': user.username,
            'image': user.gifs.latest_gif(),
        }

    return render_to_response('gifs/index.html', { 'users': user_data })

def user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404

    images = user.gifs.all()

    is_owner = request.user.is_authenticated() and user == request.user

    return render_to_response('gifs/user.html', {
        'user': user,
        'images': images,
        'is_owner': is_owner,
    })
