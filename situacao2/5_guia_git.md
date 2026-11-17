# Guia do Git e GitHub

## 1. Configuração inicial (uma vez)
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```
Crie o repositório vazio `helpdesk-pi2` em github.com (público) e copie a URL.

## 2. Estrutura recomendada
```
helpdesk-pi2/
├── README.md
├── situacao1/        # plano, casos de uso, sequência, protótipo, projeto de dados
├── situacao2/        # código: app/, tests/, schema.sql, run.py, requirements.txt, manual
└── situacao3/        # formulários, relatório de testes, PDF das opiniões, links dos vídeos
```
Os arquivos de código (`app/`, `tests/`, `schema.sql`, `run.py`, `requirements.txt`) podem ficar em `situacao2/`. Ajuste o caminho ao rodar (`cd situacao2`).

## 3. Primeiro envio
```bash
cd helpdesk-pi2
git init -b main
git add .
git commit -m "Situação 1: plano, UML, protótipo e projeto de dados"
git remote add origin https://github.com/SEU_USUARIO/helpdesk-pi2.git
git push -u origin main
```

## 4. Commits por situação
```bash
git add situacao2/
git commit -m "Situação 2: CRUD de chamados em MVC com testes"
git add situacao3/
git commit -m "Situação 3: formulários de teste e correções"
git push
```

## 5. Boas práticas
- Faça commits pequenos, com mensagens que dizem o que mudou.
- Não suba o banco (`*.db`) nem o `.venv/`. O `.gitignore` já cuida disso.
- Os vídeos são pesados: suba no YouTube (não listado) ou Drive e coloque o link no `README.md`.
- Mantenha o `README.md` na raiz com o tema, como rodar e o link dos vídeos.
