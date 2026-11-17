# Manual de Uso: Help Desk

## Instalação
1. Instale o Python 3.10 ou superior.
2. Na pasta do projeto: `python -m venv .venv` e ative (`source .venv/bin/activate` ou `.venv\Scripts\activate` no Windows).
3. `pip install -r requirements.txt`
4. `python run.py` e abra `http://127.0.0.1:5000`.

## Abrir um chamado
1. Clique em **+ Novo chamado**.
2. Preencha **título** (até 100 caracteres), **solicitante**, **descrição** e **prioridade**.
3. Clique em **Salvar**. A mensagem "Chamado aberto com sucesso." aparece e o chamado entra na lista com status `aberto`.
4. Se faltar algum campo, o formulário mostra o erro ao lado do campo e mantém o que você digitou.

## Ver e filtrar chamados
A tela inicial lista do mais novo ao mais antigo. A cor da borda indica a prioridade: vermelho (alta), amarelo (média), verde (baixa). Use os botões **aberto**, **em andamento** e **resolvido** para filtrar, ou **Todos** para limpar o filtro.

## Alterar o status
No cartão do chamado, escolha o novo status na lista e clique em **Salvar**.

## Editar um chamado
Clique em **Editar**, altere os campos e clique em **Salvar**. O status não muda por aqui, use a lista do cartão.

## Excluir um chamado
Clique em **Excluir** e confirme no diálogo. A exclusão é permanente.

## Mensagens e erros
| Mensagem | Significado |
|---|---|
| Informe um título de até 100 caracteres | Título vazio ou longo demais |
| Descreva o problema | Descrição vazia |
| Informe o solicitante (até 80 caracteres) | Solicitante vazio ou longo demais |
| Prioridade inválida | Valor fora de baixa, média ou alta |
| Status inválido | Status fora dos três permitidos |

## Rodar os testes
`pytest -v` (devem passar 7 testes).
