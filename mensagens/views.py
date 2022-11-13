from django.shortcuts import render


# página de mensagens
def mensagens(request):
    return render(request, 'mensagens/mensagens.html')
