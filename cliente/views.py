from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# Create your views here.

def fcliente(request):
    clientes = Cliente.objects.all()
    return render(request, "rel_cliente.html",{"clientes":clientes})

def Fcadcliente(request):
    return render(request, "cad_cliente.html")

def salvar(request):
    vnome = request.POST.get("nome")
    vtelefone = request.POST.get("telefone")
    vemail = request.POST.get("email")
    vsenha = request.POST.get("senha")

    senha_criptografada = make_password(vsenha)
    if vnome:
        Cliente.objects.create(nome=vnome, telefone=vtelefone, email=vemail, senha=senha_criptografada)

    return redirect(fcliente)

def exibir(request, id=None):
    if id is None:
        id = request.session.get('cliente_id')

    if id is not None:
        try:
            cliente = Cliente.objects.get(id=id)
            return render(request, "updateC.html", {"cliente": cliente})
        except Cliente.DoesNotExist:
            messages.error(request, 'Cliente não encontrado')
            return redirect('findex')
    else:
        messages.error(request, 'Você não está Logado!')
        return redirect('flogcliente')

def update(request, id):
    vnome = request.POST.get("nome")
    vtelefone = request.POST.get("telefone")
    vemail = request.POST.get("email")
    cliente = Cliente.objects.get(id=id)
    cliente.nome = vnome
    cliente.telefone = vtelefone
    cliente.email = vemail
    cliente.save()
    return redirect(fcliente)


def excluir(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect(fcliente)

def flogcliente(request):
    return render(request, 'LogCliente.html')

def logar(request):
    if request.method == 'POST':
        email = request.POST.get("nome")
        senha = request.POST.get("senha")

        try:
            cliente = Cliente.objects.get(email=email)
            if cliente.check_password(senha):
                request.session['cliente_id'] = cliente.id #ADICIONEI SESSÃO
                request.session['cliente_nome'] = cliente.nome
                return redirect('ftelacli')
            else:
                return redirect('flogcliente')

        except Cliente.DoesNotExist:
            messages.error(request, 'Credenciais Inválidas.')
            return redirect('flogcliente')

def logout(request):
    try:
        del request.session['cliente_id']
        del request.session['cliente_nome']
    except KeyError:
        pass
    return redirect('flogcliente')


def ftelacli(request):
    if 'cliente_id' not in request.session:
        return redirect('flogcliente')
    return render(request, "telacliente.html")
