from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from .models import User
from .forms import AuthForm


class RegistrationView(View):
    def _render(self, request, form=None, is_success=False):
        return render(request, "app/registration.html", {
            "form": form or AuthForm(),
            'is_success': is_success
        })

    def get(self, request, *args, **kwargs):
        return self._render(request)

    def post(self, request, *args, **kwargs):
        is_success = False
        form = AuthForm()
        message = None
        if request.method == 'POST':
            form = AuthForm(request.POST)
            try:
                if form.is_valid():
                    User.objects.create_user(**form.cleaned_data)
                    is_success = True
            except:
                message = 'Пожалуйста, исправьте ошибки'

        return render(request, 'app/registration.html', {
            'form': form,
            'is_success': is_success,
            'message': message
        })


def login_view(request):
    form = AuthForm()
    message = None
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is None:
                message = "Электронная почта или пароль неправильные"
            else:
                login(request, user)
                next_url = '/'
                if 'next' in request.GET:
                    next_url = request.GET.get("next")
                return redirect(next_url)
    return render(request, "app/login.html", {
        "form": form,
        'message': message
    })


def logout_view(request):
    logout(request)
    return redirect('login')
