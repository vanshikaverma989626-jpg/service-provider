from accounts.models import Profile


def user_profile(request):
    user = getattr(request, 'user', None)
    profile = None

    if user and user.is_authenticated:
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            profile = None

    return {
        'user_profile': profile,
    }
