# Plano de Projeto Atualizado: Help Desk
Projeto Integrador Transdisciplinar em Engenharia de Software II · versão 2.0 · 17/11/2026

## 1. Visão geral
Sistema web para registrar, acompanhar e resolver chamados de suporte, substituindo controles informais (planilhas, mensagens) por um fluxo único com prioridade e status.

## 2. Objetivos
- **Geral:** entregar uma aplicação web funcional, testada e documentada para gestão de chamados.
- **Específicos:** (1) abrir, listar, filtrar, editar e excluir chamados; (2) validar dados na entrada; (3) aplicar o padrão MVC; (4) validar a solução com 5 usuários.

## 3. Escopo
| Dentro do escopo | Fora do escopo (versão atual) |
|---|---|
| CRUD de chamados, filtro por status, prioridade por cor, validação, testes automatizados | Login e perfis de acesso, anexos, notificações por e-mail, relatórios gerenciais |

## 4. Requisitos
- **Funcionais:** RF01 abrir chamado · RF02 listar e filtrar · RF03 editar · RF04 alterar status · RF05 excluir com confirmação.
- **Não funcionais:** RNF01 usabilidade (mensagens claras) · RNF02 validação de entrada · RNF03 manutenibilidade (MVC e testes) · RNF04 portabilidade (roda em qualquer SO com Python 3).

## 5. Tecnologias
Python 3 · Flask · SQLite · HTML/CSS (Jinja) · pytest · Git/GitHub. Escolhidas por serem populares, bem documentadas e de fácil manutenção.

## 6. Cronograma sugerido
| Fase | Atividade | Duração |
|---|---|---|
| Situação 1 | Revisão do plano, UML, IHC, modelo de dados | 1 semana |
| Situação 2 | Codificação, testes, repositório, vídeo | 2 semanas |
| Situação 3 | Teste com 5 pessoas, correções, documentação final, vídeo | 1 semana |

## 7. Riscos
| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Testadores não responderem a tempo | Média | Alto | Convidar 7 pessoas para garantir 5 respostas |
| Bugs encontrados tarde | Média | Médio | Testes automatizados desde a Situação 2 |
| Falta de tempo para os vídeos | Média | Médio | Usar os roteiros prontos e gravar em uma sessão |
| Perda de código | Baixa | Alto | Commits frequentes no GitHub |

## 8. Melhoria contínua (Kaizen): comparação ilustrativa entre versões de planejamento
A coluna v1.0 representa uma referência conceitual de planejamento, não uma entrega comprovada do PI I. A documentação original do PI I não foi fornecida.

| Item | v1.0 (ponto de partida) | v2.0 (esta entrega) |
|---|---|---|
| Escopo | Ideia geral de um sistema de chamados | Escopo delimitado, com itens fora do escopo explícitos |
| Modelagem UML | Apenas diagrama de classes | Classes, casos de uso e sequência (abrir chamado e alterar status) |
| IHC | Tela de lista e formulário | Protótipo de 4 telas, com erro de validação e confirmação de exclusão |
| Dados | Tabela única sem regras formais | DER, modelo lógico em 3FN, DDL com CHECK e dicionário de dados |
| Testes | Nenhum | testes automatizados; validação com 5 usuários ainda pendente |

**Próximo ciclo:** as sugestões coletadas na Situação 3 entram aqui como v2.1, com as correções feitas.

## 9. Critérios de aceite
Os 5 requisitos funcionais operando, testes automatizados passando e 5 formulários de teste a coletar e documentação versionada no Git.
