from django.urls import path

from . import views

app_name = 'perfil'

urlpatterns = [

    path('coletor/novo',
        views.RegistroColetor.as_view(),
        name='coletor_registro'
    ),

    path('coletor/editar',
        views.EditarColetor.as_view(),
        name='coletor_edicao'
    ),
    
    path('consumidor/novo',
        views.RegistroConsumidor.as_view(),
        name='consumidor_registro'
    ),

    path('consumidor/editar',
        views.EditarConsumidor.as_view(),
        name='consumidor_edicao'
    ),

]

# views relativas ao processo de autenticação e administração se senhas
urlpatterns += [
    path('entrar/', views.UsuarioLoginView.as_view(), name='login'),
    path('sair/', views.UsuarioLogoutView.as_view(), name='logout'),
    path('alterar-senha/', views.UsuarioPasswordChangeView.as_view(), name='password_change'),
    path('alterar-senha/sucesso/', views.UsuarioPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('resetar-senha/', views.UsuarioPasswordResetView.as_view(), name='password_reset'),
    path('resetar-senha/<uidb64>/<token>/', views.UsuarioPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('resetar-senha/concluido/', views.UsuarioPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('resetar-senha/sucesso/', views.UsuarioPasswordResetDoneView.as_view(), name='password_change_done'),
]
