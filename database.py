# db.py
import psycopg2

def conectar():
    try:
        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            port=port
        )
        print("Conexão estabelecida com sucesso! ✅")
        return conn
    except Exception as e:
        print("Erro ao conectar no PostgreSQL:", e)
        return None


host = "localhost"      
dbname = "postgres"     
user = "postgres"     
password = "1977" 
port = "5432"            
options="client_encoding=UTF8"

try:    
    conn = psycopg2.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password,
        port=port
    ) 
    
    cur = conn.cursor()
    
    cur.execute("SELECT version();")
    versao = cur.fetchone()
    print("Conectado ao PostgreSQL - Versão:", versao)

    
    cur.close()
    conn.close()

except Exception as e:
    print("Erro ao conectar no PostgreSQL:", e)
  


