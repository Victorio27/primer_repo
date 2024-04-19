from .models import Avatar

def avatar_context(request):
    avatar_url = None
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user.id)
        avatar_url = avatares[0].imagen.url if avatares.exists() else None
    return {'avatar_url': avatar_url}

