class BancoDeDados:
  def __init__(self):
    self.server = 'localhost'
    self.database = 'Imediato'
    self.username = 'sa'
    self.password = 'joaosoares2007'
    self.driver = '{SQL Server}'
    self.conn_str = f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'