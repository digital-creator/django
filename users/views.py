from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm
from django.contrib import auth


def user_login(request):
    form = None
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = auth.authenticate(username=data['username'],
                                     password=data['password'])
            print(user)
            if user.is_authenticated:
                if user.is_client:
                    return HttpResponseRedirect(reverse('client'))
                elif user.is_player:
                    return HttpResponseRedirect(reverse('player'))
                elif user.is_supplier:
                    return HttpResponseRedirect(reverse('supplier'))
        else:
            print("Not valid")

    else:

        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)
# Create your views here.
