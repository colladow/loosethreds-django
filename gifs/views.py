"""
Views for the gifs app.
"""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import Http404, HttpResponseForbidden
from django.template import RequestContext

from gifs.models import Gif
from lib import download_gif

def index(request):
    """
    Serves the home page. Shows the latest image
    for each user of the app.
    """
    users = User.objects.all()
    user_data = {}

    for user in users:
        user_data[user.pk] = {
            'username': user.username,
            'image': user.gifs.latest_gif(),
        }

    return render_to_response('gifs/index.html',
                              { 'users': user_data },
                              context_instance=RequestContext(request))

def show_user(request, user_id):
    """
    Shows all images for a single user.
    """
    user = get_object_or_404(User, pk=user_id)

    images = user.gifs.all()

    is_owner = request.user.is_authenticated() and user == request.user

    return render_to_response('gifs/user.html', {
        'this_user': user,
        'images': images,
        'is_owner': is_owner,
    }, context_instance=RequestContext(request))

@login_required
def delete(request, user_id, image_id):
    """
    Deletes an image that belongs to the authenticated user.
    """
    user = get_object_or_404(User, pk=user_id)

    if user != request.user:
        return HttpResponseForbidden('This is not your image.')

    if request.method != 'POST':
        return HttpResponseForbidden('Bad method.')

    if request.POST['_method'] != 'delete':
        return HttpResponseForbidden('Bad method')

    try:
        image = request.user.gifs.get(pk=image_id)
    except Gif.DoesNotExist:
        raise Http404

    image.image.delete()
    image.delete()

    return redirect('/users/' + user_id)

@login_required
def create(request, user_id):
    """
    Creates a new image.
    """
    user = get_object_or_404(User, pk=user_id)

    if user != request.user:
        return HttpResponseForbidden('This is not you.')

    if request.method != 'POST':
        return HttpResponseForbidden('Bad method.')

    if request.FILES.has_key('image'):
        uploaded = request.FILES['image']

        name, gif_file = uploaded.name, uploaded
    else:
        name, gif_file = download_gif(request.POST['url'])

    gif = user.gifs.create()
    gif.image.save(name, gif_file)

    return redirect('/users/' + user_id)
