from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from accounts.forms import SignupForm, UserForm, ProfileForm, AuthenticationForm
from accounts.models import Profile


def register(request):  # ou appeler  signin
    if request.method == 'POST':  # save
        form = SignupForm(request.POST)
        if form.is_valid():  # si valide  alors save
            form.save()  # save le new user  mais sans login
            mon_username = form.cleaned_data['username']  # extraire username depuis le form
            mon_password = form.cleaned_data['password1']  # extraire password depuis le form
            user = authenticate(username=mon_username, password=mon_password)  # préparer le user
            login(request, user)  # faire le login
            messages.success(request, 'created')  # qui sera affiché dans redirect template
            return redirect('/accounts/profile')  # redirect vers ...
    else:  # show form
        form = SignupForm()
    return render(request, 'accounts/registration/register.html', {'form': form})


@login_required
def profile(request):
    storage = messages.get_messages(request)
    profile_ = Profile.objects.get(user=request.user)  # get profile qui a user(dans profile) = au user request
    return render(request, 'accounts/profile/profile.html', {'profile': profile_, 'messages': storage})


def login_view(request):
    context = {}
    user = request.user  # si request.user est authenticated alors ==> profile
    if user.is_authenticated:  # si request.user est authenticated alors ==> profile
        return redirect("home")  # si request.user est authenticated alors ==> profile
    if request.POST:
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)  # authenticated
            if user:
                login(request, user)
                messages.success(request, 'login in the site')  # qui sera affiché dans redirect template
                return redirect("accounts:profile")  # REDIRECT to home
    else:  # request.GET:
        form = AuthenticationForm()   # form vide
    context = {'form': form}
    return render(request, "accounts/registration/login.html", context)


#  #$#       view de logout utilisé dans  => logout.html et meme dans base.html
def logout_view(request):
    logout(request)
    messages.success(request, 'you are logged out')  # qui sera affiché dans redirect template
    return redirect('home')


@login_required
def profile_edit(request):
    profile_ = Profile.objects.get(user=request.user)  # get profile qui a user(dans profile) = au user request
    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile_)  # request.FILES : pour uplaod file
        if userform.is_valid() and profileform.is_valid():
            userform.save()  # save user directement mais le profile nécessité la suivante
            myform = profileform.save(commit=False)  # s'assurer que le profile est relié au user
            myform.user = request.user  # s'assurer que le profile est relié au user
            myform.save()  # save profile
            messages.success(request, 'updated')  # qui sera affiché dans redirect template
            return redirect('accounts:profile')
    else:  # (affichage)
        userform = UserForm(instance=request.user)  # request.user = data du user connecté (affichage)
        profileform = ProfileForm(instance=profile_)  # profile_ = profile du user connecté  (affichage)
    return render(request, 'accounts/profile/edit_profile.html', {'userform': userform, 'profileform': profileform})

# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important! conserver la session aprés le changement
#             # messages.success(request, 'Your password was successfully updated!')
#             return redirect('/accounts/profile')
#         else:
#             return redirect('/accounts/change_password')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'accounts/registration/change_password.html', {'form': form})
