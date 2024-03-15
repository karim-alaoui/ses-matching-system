from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

def superuser_required(user):
    return user.is_superuser

@login_required
@user_passes_test(superuser_required)
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('some-view')

    return render(request, 'register.html')
