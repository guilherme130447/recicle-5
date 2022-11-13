from django.shortcuts import render


# página de contato
def contato(request):
    return render(request, 'contatos/contato.html')


# página de lgpd
def lgpd(request):
    return render(request, 'contatos/lgpd.html')
