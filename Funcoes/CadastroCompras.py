import pyodbc

from ConexaoBancoDados import BancoDeDados
from RetornaProximoNumeroProdutos import ProximoProduto
bancoDeDados = BancoDeDados()
proximoProduto = ProximoProduto()

class CadastroCompras:
  def __init__(self, nomeProduto, unidadeMedida, quantidade, precoUnitario):
    self.nomeProduto = nomeProduto
    self.unidadeMedida = unidadeMedida
    self.quantidade = quantidade
    self.precoUnitario = precoUnitario
    self.conn_str = bancoDeDados.conn_str

  def validacoes(self):
    conn = pyodbc.connect(self.conn_str)
    cursor = conn.cursor()

    # Verificar se o produto já existe na tabela de "produtos"
    select_produto_query = 'SELECT prdcode FROM produtos WHERE prdnome = ? '
    cursor.execute(select_produto_query, self.nomeProduto.strip())
    resultado = cursor.fetchone()

    if resultado:
        PrdCode = resultado[0]
    else:
        PrdCode = proximoProduto.ProximoValor()
        #Chamar classe para cadastrar produto

    # Fechar a conexão
    conn.close()

  '''
  def cadastro(self):
    conn = pyodbc.connect(self.conn_str)
    cursor = conn.cursor()

    # Instrução SQL para inserir informações de venda
    insert_venda_query = 
    INSERT INTO vendas (nome_produto, quantidade, preco_unitario)
    VALUES (self.nomeProduto, self.quantidade, self.precoUnitario)
    
    
    # Executar a instrução SQL
    cursor.execute(insert_venda_query, self.nomeProduto, self.quantidade, self.precoUnitario)
    #conn.commit()
    '''