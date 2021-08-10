from django.shortcuts import render


def profile(request):
    context = {
        'name': 'Profile Page'
    }
    return render(request, 'login.html', context)
