from django.shortcuts import render, redirect
from .models import Produto

# Create your views here.

def fproduto(request):
    produtos = Produto.objects.all()
    return render(request, "rel_produto.html", {"produtos":produtos})

def Fcadproduto(request):
    return render(request, "cad_produto.html")

def salvarP(request):
    vnome = request.POST.get("nome")
    vdescricao = request.POST.get("descricao")
    vpreco = request.POST.get("preco")
    vquantidade = request.POST.get("quantidade")
    vcategoria = request.POST.get("categoria")
    vimagem = request.FILES.get("imagem")
    if vnome:
        Produto.objects.create(

            nome=vnome,
            descricao=vdescricao,
            preco=vpreco,
            quantidade=vquantidade,
            categoria=vcategoria,
            imagem=vimagem

        )

    return redirect(fproduto)

def exibirP(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, "updateP.html", {"produtos": produto})

def updateP(request, id):
    vnome = request.POST.get("nome")
    vdescricao = request.POST.get("descricao")
    vpreco = request.POST.get("preco")
    vquantidade = request.POST.get("quantidade")
    vcategoria = request.POST.get("categoria")
    vimagem = request.FILES.get("imagem")

#================================================================================#

    produto = Produto.objects.get(id=id)
    produto.nome = vnome
    produto.descricao = vdescricao
    produto.preco = vpreco
    produto.quantidade = vquantidade
    produto.categoria = vcategoria
    if vimagem:
        produto.imagem = vimagem
    produto.save()
    return redirect(fproduto)


def excluirP(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect(fproduto)


def exibir_celulares(request):
    produtos_celulares = Produto.objects.filter(categoria='celular')
    return render(request, 'exibcelular.html', {'produtos': produtos_celulares})

def exibir_capas(request):
    produtos_capas = Produto.objects.filter(categoria='capa')
    return render(request, 'exibcapas.html', {'produtos': produtos_capas})

def exibir_outros(request):
    produtos_outros = Produto.objects.filter(categoria='acessorio')
    return render(request, 'exiboutros.html', {'produtos': produtos_outros})

'''''''''
def exibir_celulares(request, categoria=None):
    if categoria:
        produtos = Produto.objects.filter(categoria=categoria)
    else:
        produtos = Produto.objects.all()
    return render(request, 'exibcelular.html', {'produtos': produtos})
'''''''''

