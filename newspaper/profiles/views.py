from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from newspaper.profiles.forms import ProfileForm
from newspaper.profiles.models import Profile


@login_required
def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)
    context = {
        'form': form,
        'profile': user_profile,
        'name': 'Profile Page',
    }
    return render(request, 'auth/profile.html', context)
