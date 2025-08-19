import fdb
from datetime import datetime
import pandas as pd

# Parâmetros do Banco
HOST = "HOST"
BD_PATH = "CAMINHO_ARQUIVO.FDB"
USER_BD = "user"
PASSWORD_BD = "password"
CHARSET = "UTF8"

# Monta o DSN
DSN = f"{HOST}:{BD_PATH}"

# Carrega a DLL do cliente Firebird (somente Windows)
fdb.load_api(r"C:\Program Files\Firebird\Firebird_2_5\bin\fbclient.dll")

# Conecta ao banco
con = fdb.connect(
    dsn=DSN,
    user=USER_BD,
    password=PASSWORD_BD,
    charset=CHARSET
)

cursor = con.cursor()

# Exemplo: buscar itens de orçamento por data
data = datetime.now().strftime(r"%Y-%m-%d")

cursor.execute("""
    SELECT 
        oi.QUANTIDADE,
        oi.CODPROD,
        p.PRODUTO
    FROM ORCAMENTO_ITENS AS oi
    JOIN PROD AS p ON p.CODPROD = oi.CODPROD
    JOIN ORCAMENTO AS o ON o.ID = oi.IDORCAMENTO
    WHERE 
        o.DATA = ?
        AND oi.DELETADO = 0;
""", (data,))

for row in cursor.fetchall():
    print(row)
