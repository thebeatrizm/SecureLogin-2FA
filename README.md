# 📲 SISTEMA DE AUTENTICAÇÃO DE DOIS FATORES (2FA) 
sistema simples em **Python** que simula uma empresa com usuários. Cada usuário deve se registrar com um dispositivo (ex.: baseado em MAC address ou ID único), fazer login com senha + código OTP (One-Time Password) enviado por email, e ter logs de acesso para detectar tentativas suspeitas. Se o dispositivo mudar, o login é bloqueado (simulando prevenção de trocas). Inclui alertas para vazamentos potenciais.

# FUNCIONALIDADES PRINCIPAIS: 
1. **Registro de Usuário:** Usuário cria conta com email, senha (hashada) e registra um dispositivo único.

2. **Login com 2FA:** Digita email/senha, recebe código OTP por email, e verifica se o dispositivo é o registrado.

3. **Verificação de Dispositivo:** Se o dispositivo não bater, login falha (simula bloqueio de trocas)

 4.**Logs de Segurança:** Registra tentativas de login (sucesso/falha) em um banco de dados, com alertas para múltiplas falhas (potencial vazamento).

# TECNOLOGIAS UTILIZADAS: 
- **Python 3.x** 
- **Bibliotecas:** pyotp (para OTP), smtplib (para emails), hashlib (para hashing), sqlite3 (banco de dados), uuid (IDs únicos).
- **Ferramentas:** GitHub para versionamento, VS Code para desenvolvimento.


## CONTRIBUIÇÕES 
**Contribuições são bem-vindas! Abra uma issue ou pull request no GitHub.** 

## LIÇENCA 📝
Este projeto é para fins educacionais e está sob a licença MIT. Use por sua conta e risco.

## AUTORA
- [BEATRIZ](https://www.linkedin.com/in/beatriz-m-a11758263) – Estudante de cybersecurity.🧜🏼‍♀️

---
Se gostou, dê uma estrela no repositório! ⭐
