# Kit para os Testadores

## 1. Mensagem de convite (WhatsApp ou e-mail)
Oi, [nome]! Preciso de 10 minutos seus. Estou finalizando um projeto da faculdade (um sistema de chamados de suporte) e preciso que alguém teste e me diga o que funciona e o que quebra. Pode ser sincero: bugs me ajudam. Acesso: [LINK OU INSTRUÇÕES]. Roteiro e formulário: [LINK DO FORMULÁRIO]. Consegue até [DATA]? Obrigada!

## 2. Como disponibilizar a aplicação
- **Mais simples:** teste por videochamada, você compartilha a tela e o testador te guia.
- **Mais prático:** rode `python run.py` e use um túnel temporário (ex.: ngrok ou Cloudflare Tunnel) para gerar um link.
- **Alternativa:** o testador baixa o projeto do GitHub e segue o `README.md`.

## 3. Roteiro de tarefas
1. Abra um novo chamado preenchendo todos os campos.
2. Tente abrir outro chamado deixando o título em branco e veja a mensagem.
3. Filtre a lista por "em andamento" e depois volte para "Todos".
4. Mude o status de um chamado para "resolvido".
5. Edite o título de um chamado.
6. Exclua um chamado, primeiro cancelando a confirmação e depois confirmando.

## 4. Formulário (copie para o Google Forms)
- Nome de quem testou (resposta curta)
- Data do teste (data)
- O que testou e funcionou: descreva a funcionalidade (parágrafo)
- O que testou e NÃO funcionou: descreva a funcionalidade e o que deve ser corrigido (parágrafo)
- Anexe um print da tela com erro, se houver (upload de arquivo)
- Funcionalidade não testada: por que faltou, ou se existe no projeto mas não foi realizada (parágrafo)
- Sugestões de melhoria (parágrafo)
- Nota geral de usabilidade de 1 a 5 (escala linear)

## 5. Depois que as respostas chegarem
Exporte as respostas em PDF (Google Forms: aba Respostas → ⋮ → imprimir) e me envie o conteúdo. Eu preencho as tabelas do `6_relatorio_de_testes.md`, o registro de bugs e a conclusão com base no que os testadores escreveram.
