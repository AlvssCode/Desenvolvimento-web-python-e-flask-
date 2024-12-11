from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente',__name__)

@cliente_route.route('/') # listar os clientes
def lista_cliente():
    return render_template('lista_cliente.html', clientes=CLIENTES)
    
@cliente_route.route('/', methods=['POST']) # inserir os dados do cliente
def inserir_cliente():
    
    data = request.json
    
    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome": data['nome'],
        "email": data['email'],
    }
    
    CLIENTES.append(novo_usuario)
    
    return render_template('item_cliente.html', cliente=novo_usuario)
    
@cliente_route.route('/new') # formulario para cadastrar um cliente
def form_cliente():
    return render_template('form_cliente.html')
    
@cliente_route.route('/<int:cliente_id>') # exibir detalhes do cliente
def detalhe_cliente(cliente_id): 
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>edit')
def form_edit_cliente(cliente_id):
    return render_template('form_edit_cliente.html')
    
@cliente_route.route('/<int:cliente_id>/update', methods=['PUT']) # atualizar informação do cliente
def atualizar_cliente(cliente_id): 
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE']) # deletar informação do cliente
def deletar_cliente(cliente_id):
    pass