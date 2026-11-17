> **Aviso de revisão (17/11/2026):** os resultados automatizados abaixo foram relatados na conversa anterior com o Claude, mas não puderam ser reexecutados neste ambiente por indisponibilidade do Flask. As avaliações com cinco pessoas permanecem pendentes.

# Relatório de Testes: Help Desk

## 1. Estratégia (Modelo V)
| Nível | Tipo | Como foi feito |
|---|---|---|
| Código | Teste unitário | pytest sobre `models.py` |
| Integração | Teste de integração | pytest com o cliente HTTP do Flask |
| Aceitação | Validação com usuários | 5 pessoas usando `docs/template_teste.md` |

## 2. Testes automatizados
| # | Teste | Verifica | Resultado |
|---|---|---|---|
| 1 | test_validar_ok | Dados válidos não geram erro | Passou |
| 2 | test_validar_campos_invalidos | Campos vazios e prioridade inválida geram erros | Passou |
| 3 | test_crud_model | Criar, obter, mudar status, excluir e rejeitar status inválido | Passou |
| 4 | test_criar_via_http | POST /novo grava e redireciona | Passou |
| 5 | test_erro_tratado_no_formulario | Título vazio retorna 400 com mensagem | Passou |
| 6 | test_404 | Chamado inexistente retorna 404 | Passou |
| 7 | test_fluxo_status_e_exclusao | Filtro por status e exclusão | Passou |

Execução: `pytest -v` → **7 passed**.

## 3. Testes com usuários
| # | Testador | Data | Funcionou | Não funcionou | Não testado |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

## 4. Registro de bugs e melhorias
| ID | Relatado por | Descrição | Print | Tipo (bug/melhoria) | Decisão (corrigir/adiar/descartar) | Commit da correção |
|---|---|---|---|---|---|---|
| B01 | | | | | | |

## 5. Mudanças adotadas
Liste aqui, em ordem, cada correção feita e onde ela está no código. Esta lista é a base do vídeo 2.

## 6. Conclusão
Resuma o que o processo mostrou: percentual de funcionalidades aprovadas, principais falhas encontradas e lições aprendidas. Não esconda as falhas: o PDF da disciplina pede isso explicitamente.
