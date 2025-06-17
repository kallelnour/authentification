from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('espace_personnel')
        else:
            error = "Nom d'utilisateur ou mot de passe incorrect"
            return render(request, 'accounts/login.html', {'error': error})

    return render(request, 'accounts/login.html')
@login_required
def edit_profile(request):
    profile = request.user.profile  # Le profil lié à l'utilisateur connecté
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('espace_personnel')  # Redirige vers la page perso
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def espace_personnel(request):
    user = request.user
    profile = user.profile
    return render(request, 'accounts/espace.html', {
        'user': user,
        'profile': profile
    })