from flask import request, render_template #Permite rodar os HTMLs criados, assim exibindo as informações do Banco em uma págine WEB
from database.db import db
from models.classificacao import Classificacao


#Irá rodar o pag WEB a fim de exibir o CRUD do banco
def classificacaoHtmlController():
    if request.method == 'GET':
         return render_template('CRUDClassificacao.html')


#Essa função contém o CRUD completo da tabela "classificacao"
def classificacaoController():

    # POST
    # ----------------------------------------------------------------------------------------------------------------------------------
    if request.method == 'POST':
            try:
                data = request.get_json()
                print(data)
                user = Classificacao(data['codigo'], data['nome'])
                db.session.add(user)
                db.session.commit()  #manda as informações para o banco de dados
                return 'Classificação criada com sucesso', 200
            except Exception as e:
                return 'Não foi possível criar uma nova classificação{}'.format(str(e)), 405
    


    # GET
    # ----------------------------------------------------------------------------------------------------------------------------------
    # elif request.method == 'GET':
    #     try:
    #         data = int(request.args.to_dict().get('codigo'))
    #         classificacao = Classificacao.query.all(data)
    #         if classificacao is None:  # Usando 'is' para verificar se a categoria é None
    #             return {'error': 'Categoria não encontrada'}, 404
    #         categorias = [{'codigo': categoria.codigo, 'descricao': categoria.descricao} for categoria in data]
    #         print(categorias)
    #     except Exception as e:
    #         return 'Não foi possível buscar pelas categorias. Error: {}'.format(str(e)), 405
    


    # PUT
    # ----------------------------------------------------------------------------------------------------------------------------------
    elif request.method == 'PUT':
          try:
              #Incialmente, a categoria será localizado pelo seu código
              id_classificacao = int(request.args.to_dict().get('codigo'))
              data = request.get_json()
              print(id_classificacao)

              classificacao = Classificacao.query.get(id_classificacao)
              if classificacao is None: #Caso o número seja inválido, um erro é informado
                  return {'error': 'Categoria não encontrada'}, 404
              print(data)
              #Se não, os campos de codigo e descrição são atualizados com novas informações digitadas pelo usuário
              classificacao.nome = data.get('nome', classificacao.nome)
              print(classificacao.codigo, classificacao.nome)
              db.session.commit() #Finaliza o processo
              return {
                   "message": "Classificação atualizada com sucesso",
                   "status": 200
              }
          except Exception as e:
              return 'Não foi possível atualizar a classificação. ERRO:{}'.format(str(e)),405



    # DELETE
    # ----------------------------------------------------------------------------------------------------------------------------------
    elif request.method == 'DELETE':
        try:
            data = int(request.args.to_dict().get('codigo'))
            classificacao = Classificacao.query.get(data)
            if classificacao is None: 
                return {'error': 'Classificação não encontrada'}, 404
            db.session.delete(classificacao)
            db.session.commit()
            return 'Classificação deletada com sucesso', 200
        except Exception as e:
            return 'Não foi possível deletar a classificação. ERRO: {}'.format(str(e)), 405 