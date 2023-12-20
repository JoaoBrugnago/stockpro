import pyodbc

from ConexaoBancoDados import BancoDeDados
bancoDeDados = BancoDeDados()

class ProximaCompra:
  def __init__(self):
    self.conn_str = bancoDeDados.conn_str

  def proximoValor(self):
    conn = pyodbc.connect(self.conn_str)
    cursor = conn.cursor()

    select_ultimo_cmpcode = 'SELECT TOP 1 cmpcode FROM compras ORDER BY cmpcode DESC'
    cursor.execute(select_ultimo_cmpcode)
    resultado = cursor.fetchone()

    CmpCode = int(resultado[0]) + 1 if resultado else 1
    conn.close()
    
    return CmpCode
