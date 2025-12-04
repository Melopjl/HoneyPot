# 🟣 HoneySpot – SSH Honeypot  
Um servidor SSH falso projetado para registrar tentativas de acesso não autorizado.  
Focado em simplicidade, performance e logs detalhados para análise de segurança.

---

<p align="center">
  <img src="https://img.shields.io/badge/Status-Online-8A2BE2?style=for-the-badge&logo=power" />
  <img src="https://img.shields.io/badge/Python-3.10+-FFD43B?style=for-the-badge&logo=python&logoColor=black" />
  <img src="https://img.shields.io/badge/Security-Honeypot-FF0050?style=for-the-badge&logo=shield" />
  <img src="https://img.shields.io/badge/Logs-JSON-00FFFF?style=for-the-badge&logo=json" />
  <img src="https://img.shields.io/badge/License-MIT-00FF66?style=for-the-badge&logo=scroll" />
</p>

---

# ⚡ Visão Geral
O **HoneySpot** simula um servidor SSH e registra de forma segura:

- Usuário informado  
- Senha informada  
- Endereço IP de origem  
- Porta usada  
- Data e hora  
- Tentativas consecutivas  

Ideal para estudos de segurança, análise de ataques automatizados e monitoramento.

---


# 🛠️ Instalação

### 1. Clonar o repositório:
```bash
git clone https://github.com/SEUUSER/HoneySpot
cd HoneySpot
```

### 2. Criar ambiente virtual (opcional):
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux
```

### 3. Instalar dependências:
```bash
pip install -r requirements.txt
```

### 4. Iniciar o honeypot:
```bash
python honeypot.py
```

---

# 🧪 Exemplo de registro criado

```json
{
  "timestamp": "2025-12-03 14:55:02",
  "ip": "189.22.10.88",
  "username": "root",
  "password": "123456",
  "port": 2222
}
```

---

# 🖥️ Aparência e saída do terminal

O projeto inclui uma interface de terminal estilizada e organizada, com feedback claro de cada tentativa de conexão:

```
████ HoneySpot v2.0 ████
[LISTENING] 0.0.0.0:2222
[ATTEMPT] root : 123456 @ 189.22.10.88
[SAVED] logs/attempts.json
```

---

# 🔒 Segurança
- Não autentica usuários  
- Não executa comandos  
- Não oferece shell real  
- Apenas registra e fecha a conexão  
- Seguro para laboratório, servidores e análise educacional  

---

# 📈 Roadmap
- [ ] Interface web opcional  
- [ ] Visualização de logs  
- [ ] Exportação para CSV  
- [ ] Suporte a múltiplas portas  
- [ ] Detector de tentativas repetidas  

---

# 📄 Licença
MIT — Livre para modificar e utilizar como quiser.

---

# 💬 Contribuição
Pull requests são bem-vindos.  
Para sugestões e melhorias, abra uma issue no repositório.
