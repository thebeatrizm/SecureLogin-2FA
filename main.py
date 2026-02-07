import sqlite3
import hashlib
import uuid
import random
import smtplib

# Banco de dados
conn = sqlite3.connect("security_logs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    email TEXT PRIMARY KEY,
    password_hash TEXT,
    device_id TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    status TEXT,
    reason TEXT
)
""")
conn.commit()

# Função para hash da senha
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Registro de usuário
def register_user(email, password, device_id):
    cursor.execute("INSERT INTO users VALUES (?, ?, ?)", 
                   (email, hash_password(password), device_id))
    conn.commit()
    print(f"Usuário {email} registrado com sucesso!")

# Simulação de envio de OTP por email
def send_otp(email):
    otp = str(random.randint(100000, 999999))
    print(f"[SIMULAÇÃO] OTP enviado para {email}: {otp}")
    return otp

# Login com 2FA
def login(email, password, device_id):
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()
    
    if not user:
        log_attempt(email, "FAIL", "Usuário não encontrado")
        return False
    
    stored_hash, registered_device = user[1], user[2]
    
    if hash_password(password) != stored_hash:
        log_attempt(email, "FAIL", "Senha incorreta")
        return False
    
    if device_id != registered_device:
        log_attempt(email, "FAIL", "Dispositivo não reconhecido")
        return False
    
    otp = send_otp(email)
    user_input = input("Digite o OTP recebido: ")
    
    if user_input == otp:
        log_attempt(email, "SUCCESS", "Login bem-sucedido")
        print("Login autorizado!")
        return True
    else:
        log_attempt(email, "FAIL", "OTP incorreto")
        return False

# Logs
def log_attempt(email, status, reason):
    cursor.execute("INSERT INTO logs (email, status, reason) VALUES (?, ?, ?)", 
                   (email, status, reason))
    conn.commit()
    print(f"[LOG] {email} - {status}: {reason}")

# Exemplo de uso
if __name__ == "__main__":
    device_id = str(uuid.uuid4())  # Simula ID único do dispositivo
    register_user("teste@empresa.com", "senha123", device_id)
    login("teste@empresa.com", "senha123", device_id)