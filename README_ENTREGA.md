# Projeto Integrador Transdisciplinar em Engenharia de Software II
## Sistema de Controle de Chamados — Help Desk

Pacote revisado em 17/11/2026 com base no enunciado fornecido.

### Estrutura
- `situacao1/`: plano, UML, DER, projeto de dados e protótipo
- `situacao2/pi2/`: aplicação Flask, esquema SQLite, testes e README técnico; `situacao2/`: manual, roteiro e Git
- `situacao3/`: revisão técnica, relatório de validação e kit de avaliadores

### Rodar no Windows (PowerShell)
```powershell
cd situacao2/pi2
py -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m pytest -v
.\.venv\Scripts\python run.py
```
Abra http://127.0.0.1:5000

### Pendências que exigem ações externas
1. Publicar o repositório GitHub e fornecer o link.
2. Gravar vídeo narrado de **pelo menos 5 minutos** demonstrando o código e funcionamento (Situação 2).
3. Convidar cinco pessoas reais, coletar nome, data, funcionalidades que funcionaram, falharam e não foram testadas, com evidências quando aplicável.
4. Incorporar melhorias a partir do feedback efetivamente coletado e exportar as cinco avaliações em PDF.
5. Gravar vídeo de até 5 minutos mostrando o funcionamento e as mudanças da Situação 3.
6. Conferir o modelo de Atividade de Entrega disponível no AVA (não foi fornecido).

**Não afirmar que o projeto é continuação de um PI I documentado sem ter o material original.** A comparação 1.0 → 2.0 é um registro interno da evolução desta proposta.

### Verificação desta revisão
A sintaxe Python e as restrições SQL foram verificadas localmente. Os testes pytest da aplicação **não puderam ser executados** neste ambiente, pois o Flask não está instalado e a instalação de dependências ficou indisponível. Rode `python -m pytest -v` no seu computador antes da entrega.
