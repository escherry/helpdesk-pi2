# Revisão técnica — 17/11/2026

## Problemas identificados na revisão
1. Validação de descrição sem limite máximo: a versão original permitia entrada excessiva.
2. Esquema SQL não tinha restrições de tamanho e texto não vazio para título, descrição e solicitante.
3. DER documentava uma tabela SOLICITANTE que não existia no banco implementado.
4. Documentação sugeria que testes com cinco usuários já estavam realizados; não há comprovação.

## Correções aplicadas
- Limite de 2000 caracteres na descrição, com validação de entrada e teste automatizado.
- Restrições SQL de tamanho e campos não vazios no esquema de novas bases.
- DER corrigido para refletir a entidade efetivamente implementada.
- Status dos testes com usuários explicitamente marcado como pendente.

**Observação:** alteração de `schema.sql` não migra bancos SQLite existentes; para a demonstração, utilize um banco novo ou faça migração controlada.
