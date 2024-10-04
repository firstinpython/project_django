# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, reverse
from .auth import login
from django.contrib import auth
import smash_db.models
from .backends import SettingsBackend


# Create your views here.

def loggin(request):
    if request.method == 'POST':
        if request.POST['tag'] == '':
            return render(request, 'smash_signin/welcome.html')
        try:
            user = smash_db.models.User.objects.get(username=request.POST['tag'])
            flag = True
        except:
            flag = False
        if flag:
            print(user.password)

            name = auth.authenticate(username=user.username, password='lolololol')
            if name:
                login(request, name)
                print('ok')
                return HttpResponseRedirect(reverse('user:profile'))
        else:
            model = SettingsBackend()
            name = model.authenticate(request=request, tag=request.POST['tag'])
            if name:
                login(request, name)
                print('okkkk')
                return render(request, 'smash_signin/welcome.html')
                # return profile(request)
    return render(request, 'smash_signin/welcome.html')


def profile(request):
    try:
        nn = request.user.tag_id
        flag = True
    except:
        flag = False
    if flag:
        if request.user.tag_id != '':
            user_db = smash_db.models.My_User.objects.get(tag_id=request.user.tag_id)
            full_name = f"{user_db.last_name} {user_db.first_name}"
            context = {
                'full_name': full_name,
                'user_db': user_db
            }
            return render(request, 'smash_signin/accout.html', context=context)
        else:
            return HttpResponseRedirect(reverse('user:login'))
    else:
        return HttpResponseRedirect(reverse('user:login'))
