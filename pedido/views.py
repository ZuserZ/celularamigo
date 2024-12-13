from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from carrinho.models import ItemCarrinho
from .models import Pedido

# Create your views here.


def finalizar_compra(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        messages.error(request, 'Você precisa estar logado para finalizar a compra!')
        return redirect('LogCliente')

    itens = ItemCarrinho.objects.filter(cliente_id=cliente_id)

    if not itens.exists():
        messages.error(request, 'Seu carrinho está vazio!')
        return redirect('exibir_carrinho')

    # Calcula o total e gera a descrição dos produtos
    total = sum(item.total_preco() for item in itens)
    produtos = ', '.join([f"{item.produto.nome} (x{item.quantidade})" for item in itens])

    # Salva o pedido no banco
    Pedido.objects.create(cliente_id=cliente_id, produtos=produtos, total=total)

    # Limpa o carrinho
    itens.delete()
    if 'carrinho' in request.session:
        del request.session['carrinho']

    messages.success(request, 'Compra finalizada com sucesso!')
    return redirect('exibir_carrinho')
