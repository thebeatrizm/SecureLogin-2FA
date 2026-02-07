# 🔐 Sistema de Autenticação de Dois Fatores (2FA)

Projeto educacional em **Python** que simula um sistema de login seguro em uma empresa fictícia.  
Cada usuário deve se registrar com um dispositivo único (ex.: baseado em MAC address ou ID gerado), fazer login com **senha + código OTP (One-Time Password)** e ter suas tentativas registradas em **logs de segurança**.

---

## 🎯 Objetivo
Explorar conceitos de **cibersegurança**, aplicando:
- Hash de senhas
- Autenticação em dois fatores (2FA)
- Verificação de dispositivo
- Registro de tentativas em banco de dados

---

## ⚙️ Funcionalidades Principais
1. **Registro de Usuário**  
   - Criação de conta com email, senha (hashada) e dispositivo único.
2. **Login com 2FA**  
   - Usuário digita email/senha, recebe OTP simulado e valida o código.
3. **Verificação de Dispositivo**  
   - Se o dispositivo não bater, login falha (simula prevenção de trocas).
4. **Logs de Segurança**  
   - Registra tentativas de login (sucesso/falha) em banco SQLite, com alertas para múltiplas falhas.

---

## 🖥️ Tecnologias Utilizadas
- **Python 3.x**
- Bibliotecas: `hashlib`, `uuid`, `random`, `sqlite3`, `smtplib` (simulação de envio de email)
- Ferramentas: **GitHub** para versionamento, **VS Code** para desenvolvimento

---

## 🚀 Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/thebeatrizm/SecureLogin-2FA.git
   cd SecureLogin-2FA
