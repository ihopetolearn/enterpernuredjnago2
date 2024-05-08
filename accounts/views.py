from django.shortcuts import render,redirect
from articles.models import Article
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.method == 'POST':
        arif = request.POST.get('username')
        paiman = request.POST.get('password')
        user = authenticate(username=arif,password=paiman)
        if user is None:
            context={"error":"that is not valid username password"}
            return render(request,'accounts/login.html',context)
        else:
            login(request,user)
            return redirect('/logout')
    else:
        return render(request,'accounts/login.html')




def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')
    return render(request,'accounts/logout.html')


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_object = form.save()
        return redirect("login/",user_object)
    context = {'form':form,}
    return render(request,'accounts/register.html',context)

