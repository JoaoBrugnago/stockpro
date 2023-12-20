import pyodbc

from ConexaoBancoDados import BancoDeDados
bancoDeDados = BancoDeDados()

class ProximoProduto:
  def __init__(self):
    self.conn_str = bancoDeDados.conn_str

  def ProximoValor(self):
    conn = pyodbc.connect(self.conn_str)
    cursor = conn.cursor()

    select_ultimo_prdcode_query = 'SELECT TOP 1 prdcode FROM produtos ORDER BY prdcode DESC'
    cursor.execute(select_ultimo_prdcode_query)
    resultado = cursor.fetchone()
    if resultado:
        PrdCode = resultado[0] + 1
    else:
        PrdCode = 1
    return PrdCode