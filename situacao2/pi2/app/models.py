"""MODEL: persistência e regras de validação (domínio de cada atributo)."""
import os
import sqlite3
from flask import current_app

PRIORIDADES = ("baixa", "media", "alta")
STATUS = ("aberto", "em_andamento", "resolvido")


def _conn():
    c = sqlite3.connect(current_app.config["DATABASE"])
    c.row_factory = sqlite3.Row
    return c


def init_db():
    schema = os.path.join(os.path.dirname(__file__), "..", "schema.sql")
    with _conn() as c, open(schema, encoding="utf-8") as f:
        c.executescript(f.read())


def validar(d):
    erros = {}
    if not d.get("titulo", "").strip() or len(d["titulo"]) > 100:
        erros["titulo"] = "Informe um título de até 100 caracteres."
    if not d.get("descricao", "").strip() or len(d.get("descricao", "")) > 2000:
        erros["descricao"] = "Descreva o problema (até 2000 caracteres)."
    if not d.get("solicitante", "").strip() or len(d["solicitante"]) > 80:
        erros["solicitante"] = "Informe o solicitante (até 80 caracteres)."
    if d.get("prioridade") not in PRIORIDADES:
        erros["prioridade"] = "Prioridade inválida."
    return erros


def listar(status=None):
    sql, args = "SELECT * FROM chamado", ()
    if status in STATUS:
        sql, args = sql + " WHERE status = ?", (status,)
    with _conn() as c:
        return c.execute(sql + " ORDER BY id DESC", args).fetchall()


def obter(id_):
    with _conn() as c:
        return c.execute("SELECT * FROM chamado WHERE id = ?", (id_,)).fetchone()


def criar(d):
    with _conn() as c:
        cur = c.execute(
            "INSERT INTO chamado (titulo, descricao, solicitante, prioridade) VALUES (?,?,?,?)",
            (d["titulo"].strip(), d["descricao"].strip(), d["solicitante"].strip(), d["prioridade"]),
        )
        return cur.lastrowid


def atualizar(id_, d):
    with _conn() as c:
        c.execute(
            "UPDATE chamado SET titulo=?, descricao=?, solicitante=?, prioridade=? WHERE id=?",
            (d["titulo"].strip(), d["descricao"].strip(), d["solicitante"].strip(), d["prioridade"], id_),
        )


def mudar_status(id_, status):
    if status not in STATUS:
        raise ValueError("Status inválido")
    with _conn() as c:
        c.execute("UPDATE chamado SET status=? WHERE id=?", (status, id_))


def excluir(id_):
    with _conn() as c:
        c.execute("DELETE FROM chamado WHERE id = ?", (id_,))
