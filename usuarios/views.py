from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View

from . import forms, models

# incluir os códigos aqui!


class RegistroConsumidor(View):

    def get(self, request):
        user_form = forms.UsuarioRegistrationForm()
        return render(request, 'usuarios/consumidor_registro.html', {'user_form': user_form})

    def post(self, request):
        user_form = forms.UsuarioRegistrationForm(request.POST)

        if user_form.is_valid():
            # Cria um objeto para o novo usuario, sem salvar o mesmo
            new_user = user_form.save(commit=False)

            # Define a senha escolhida
            new_user.set_password(
                user_form.cleaned_data['password']
            )

            # Salva o objeto User
            new_user.save()

            # Cria o perfil do usuario
            models.Consumidor.objects.create(usuario=new_user)

            return render(request, 'usuarios/registro_concluido.html', {'new_user': new_user})

        else:
            return render(request, 'usuarios/consumidor_registro.html', {'user_form': user_form})


class RegistroColetor(View):

    def get(self, request):
        user_form = forms.UsuarioRegistrationForm()
        return render(request, 'usuarios/coletor_registro.html', {'user_form': user_form})

    def post(self, request):
        user_form = forms.UsuarioRegistrationForm(request.POST)

        if user_form.is_valid():
            # Cria um objeto para o novo usuario, sem salvar o mesmo
            new_user = user_form.save(commit=False)

            # Define a senha escolhida
            new_user.set_password(
                user_form.cleaned_data['password']
            )

            # Salva o objeto User
            new_user.save()

            # Cria o perfil do usuario
            models.Coletor.objects.create(usuario=new_user)

            return render(request, 'usuarios/registro_concluido.html', {'new_user': new_user})

        else:
            return render(request, 'usuarios/coletor_registro.html', {'user_form': user_form})


class EditarConsumidor(LoginRequiredMixin, View):

    def get(self, request):
        account_form = forms.UsuarioEditForm(instance=request.user)
        consumer_form = forms.ConsumidorEditForm(instance=request.user.profile)

        try:
            profile_picture = True
            print(request.user.profile.profile_picture.url)
        except:
            profile_picture = False

        return render(request, 'usuarios/editar.html', {'account_form': account_form, 'consumer_form': consumer_form, 'profile_picture': profile_picture})

    def post(self, request):
        account_form = forms.UsuarioEditForm(
            instance=request.user, data=request.POST)
        consumer_form = forms.ConsumidorEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)

        if account_form.is_valid() and consumer_form.is_valid():
            account_form.save()
            consumer_form.save()

        try:
            profile_picture = True
            print(request.user.profile.profile_picture.url)
        except:
            profile_picture = False

        return render(request, 'usuarios/editar.html', {'account_form': account_form, 'consumer_form': collector_form, 'profile_picture': profile_picture})


class EditarColetor(LoginRequiredMixin, View):

    def get(self, request):
        user_form = forms.UsuarioEditForm(instance=request.user)
        collector_form = forms.ColetorEditForm(
            instance=request.user)

        try:
            profile_picture = True
            print(request.user.profile.profile_picture.url)
        except:
            profile_picture = False

        return render(request, 'usuarios/editar.html', {'user_form': user_form, 'collector_form': collector_form, 'profile_picture': profile_picture})

    def post(self, request):
        user_form = forms.UsuarioEditForm(instance=request.user, data=request.POST)
        collector_form = forms.ColetorEditForm(
            instance=request.user, data=request.POST, files=request.FILES)

        if user_form.is_valid() and collector_form.is_valid():
            user_form.save()
            collector_form.save()

        try:
            profile_picture = True
            print(request.user.profile.profile_picture.url)
        except:
            profile_picture = False

        return render(request, 'usuarios/editar.html', {'user_form': user_form, 'collector_form': collector_form, 'profile_picture': profile_picture})


class UsuarioLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form=forms.UserLoginForm


class UsuarioLogoutView(LogoutView):
    template_name = "registration/logged_out.html"


class UsuarioPasswordChangeView(PasswordChangeView):
    template_name = "registration/password_change_form.html"


class UsuarioPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "registration/password_change_done.html"


class UsuarioPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "registration/password_reset_complete.html"


class UsuarioPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "registration/password_reset_confirm.html"


class UsuarioPasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/password_reset_done.html"


class UsuarioPasswordResetView(PasswordResetView):
    template_name = "registration/password_reset_form.html"
