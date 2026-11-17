# Help Desk: Casos de Uso e Diagramas de Sequência

## 1. Diagrama de casos de uso

Ator: **Usuário** (solicitante e atendente). Os diagramas usam Mermaid e renderizam direto no GitHub.

```mermaid
flowchart LR
    U(["👤 Usuário"])
    subgraph SIS["Sistema Help Desk"]
        UC1(["UC01 Abrir chamado"])
        UC2(["UC02 Listar chamados"])
        UC3(["UC03 Filtrar por status"])
        UC4(["UC04 Editar chamado"])
        UC5(["UC05 Alterar status"])
        UC6(["UC06 Excluir chamado"])
        UC7(["Validar dados"])
    end
    U --- UC1 & UC2 & UC4 & UC5 & UC6
    UC3 -. "«extend»" .-> UC2
    UC1 -. "«include»" .-> UC7
    UC4 -. "«include»" .-> UC7
```

### Especificação resumida

| Caso de uso | Fluxo principal | Fluxo alternativo / exceção |
|---|---|---|
| UC01 Abrir chamado | Usuário preenche título, descrição, solicitante e prioridade; o sistema valida, grava com status `aberto` e exibe confirmação | Dados inválidos: o sistema mantém o formulário preenchido e mostra o erro em cada campo |
| UC02 Listar chamados | O sistema exibe os chamados do mais novo ao mais antigo, com cor por prioridade | Sem chamados: mensagem "Nenhum chamado encontrado" |
| UC03 Filtrar por status | Usuário escolhe `aberto`, `em andamento` ou `resolvido` | Status desconhecido: lista todos |
| UC04 Editar chamado | Usuário altera os campos; o sistema valida e salva | Chamado inexistente: erro 404 |
| UC05 Alterar status | Usuário seleciona o novo status e salva | Status inválido: mensagem de erro e nenhuma alteração |
| UC06 Excluir chamado | Usuário confirma no diálogo; o sistema remove | Usuário cancela: nada acontece |

## 2. Diagrama de sequência: UC01 Abrir chamado

```mermaid
sequenceDiagram
    actor U as Usuário
    participant V as View (form.html)
    participant C as Controller (novo)
    participant M as Model (models.py)
    participant DB as SQLite

    U->>V: Preenche formulário e clica em Salvar
    V->>C: POST /novo
    C->>M: validar(dados)
    M-->>C: erros
    alt sem erros
        C->>M: criar(dados)
        M->>DB: INSERT INTO chamado
        DB-->>M: id
        M-->>C: id
        C-->>V: redirect para / + mensagem de sucesso
        V-->>U: Lista com o novo chamado
    else com erros
        C-->>V: renderiza form.html (HTTP 400)
        V-->>U: Campos preservados + mensagens de erro
    end
```

## 3. Diagrama de sequência: UC05 Alterar status

```mermaid
sequenceDiagram
    actor U as Usuário
    participant V as View (index.html)
    participant C as Controller (status)
    participant M as Model (models.py)
    participant DB as SQLite

    U->>V: Escolhe novo status e clica em Salvar
    V->>C: POST /{id}/status
    C->>M: obter(id)
    M->>DB: SELECT
    DB-->>M: chamado
    alt chamado não existe
        C-->>U: HTTP 404
    else existe
        C->>M: mudar_status(id, status)
        alt status válido
            M->>DB: UPDATE chamado
            C-->>V: redirect para / + "Status alterado."
        else status inválido
            M-->>C: ValueError
            C-->>V: redirect para / + "Status inválido."
        end
        V-->>U: Lista atualizada
    end
```
