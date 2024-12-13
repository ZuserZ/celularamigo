
from django.shortcuts import render, redirect
from .models import ItemCarrinho
from produto.models import Produto
from cliente.models import Cliente
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.

def addcarrinho(request, produto_id):
    if request.method == 'POST':
        try:
            produto = Produto.objects.get(id=produto_id)
            quantidade = int(request.POST.get('quantidade', 1))

            cliente_id = request.session.get('cliente_id')
            if cliente_id:
                cliente = Cliente.objects.get(id=cliente_id)

                # Salvar no banco de dados
                item_carrinho = ItemCarrinho.objects.create(cliente=cliente, produto=produto, quantidade=quantidade)

                # Salvar na sessão
                carrinho = request.session.get('carrinho', {})

                # Adiciona ou atualiza o item no carrinho
                carrinho[str(item_carrinho.id)] = {
                    'produto_id': produto.id,
                    'nome': produto.nome,
                    'quantidade': quantidade,
                    'preco': float(produto.preco),
                }
                request.session['carrinho'] = carrinho
                request.session.modified = True  # Garante que a sessão será salva

                messages.success(request, 'Produto adicionado ao carrinho!')
            else:
                messages.error(request, 'Você precisa estar logado para adicionar produtos ao carrinho!')

        except Produto.DoesNotExist:
            messages.error(request, 'Produto não encontrado')

        return redirect('exibir_carrinho')





#def addcarrinho(request, produto_id):
#    if request.method == 'POST':
#        try:
#            produto = Produto.objects.get(id=produto_id)
#            quantidade = int(request.POST.get('quantidade', 1))
#
#            cliente_id = request.session.get('cliente_id')
#            if cliente_id:
#               cliente = Cliente.objects.get(id=cliente_id)
#                ItemCarrinho.objects.create(cliente=cliente, produto=produto, quantidade=quantidade)
#                messages.success(request, 'Produto adicionado ao carrinho!')
#            else:
#                messages.error(request, 'Você precisa estar Logado para adicionar produtos ao carrinho!')
#
#        except Produto.DoesNotExist:
#            messages.error(request, 'Produto não encontrado')
#
#        return redirect('findex')



def exibir_carrinho(request):
    cliente_id = request.session.get('cliente_id')
    if cliente_id:
        itens = ItemCarrinho.objects.filter(cliente_id=cliente_id)
        total = sum(item.total_preco() for item in itens)
        return render(request, 'carrinho.html', {'itens': itens, 'total': total})
    else:
        messages.error(request, 'Você precisa estar logado para ver o carrinho!')
        return render(request, 'LogCliente.html')


def excluirC(request, item_id):
    cliente_id = request.session.get('cliente_id')

    if not cliente_id:
        messages.error(request, 'Você precisa estar logado para remover itens do carrinho!')
        return redirect('LogCliente')

    try:
        # Verifica se o item existe no banco e pertence ao cliente logado
        item = ItemCarrinho.objects.get(id=item_id, cliente_id=cliente_id)
        item.delete()  # Remove o item do banco de dados

        # Atualiza a sessão removendo o item
        carrinho = request.session.get('carrinho', {})
        item_id_str = str(item_id)
        if item_id_str in carrinho:
            del carrinho[item_id_str]
            request.session['carrinho'] = carrinho
            request.session.modified = True

        messages.success(request, 'O item foi removido do carrinho com sucesso!')
    except ItemCarrinho.DoesNotExist:
        messages.error(request, 'Item não encontrado ou não pertence a você.')

    return redirect('exibir_carrinho')









def alterarC(request, id):
    if request.method == "POST":
        nova_quantidade = int(request.POST.get("quantidade", 1))
        try:
            item = ItemCarrinho.objects.get(id=id)
            item.quantidade = nova_quantidade
            item.save()
            return redirect('exibir_carrinho')
        except ItemCarrinho.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Item não encontrado'})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'})



