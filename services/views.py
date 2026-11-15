from django.shortcuts import render
from accounts.models import Profile, Category
from django.shortcuts import get_object_or_404
def home(request):
    providers = Profile.objects.all() # give me every profile stored in database
    return render(
        request,
        'services/home.html',
        {'providers': providers}      # sends data from view to template. (ORM query)
    )

def provider_list(request):
    providers = Profile.objects.filter(
        role='provider'
    )
    search = request.GET.get(
        'search'
    )
    category = request.GET.get(
        'category'
    )
    if search:
        providers = providers.filter(
            user__username__icontains=search
        )
    if category:
        providers = providers.filter(
            category__name=category
        )
    categories = Category.objects.all()
    return render(
        request,
        'services/provider_list.html',
        {
            'providers': providers,
            'categories': categories,
            'search_query': search,
            'selected_category': category
        }
    )

def provider_detail(request, id):
    provider = get_object_or_404(Profile,id=id) #get the object, if doesnot exist show 404 page, dont crash
    return render(
        request,
        'services/provider_detail.html',
        {
            'provider': provider
        }
    )