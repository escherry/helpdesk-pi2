"""CONTROLLER: recebe a requisição, aciona o Model e escolhe a View."""
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from . import models

bp = Blueprint("chamados", __name__)


@bp.get("/")
def index():
    status = request.args.get("status")
    return render_template("index.html", chamados=models.listar(status),
                           status=status, opcoes=models.STATUS)


@bp.route("/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        erros = models.validar(request.form)
        if not erros:
            models.criar(request.form)
            flash("Chamado aberto com sucesso.", "ok")
            return redirect(url_for("chamados.index"))
        return render_template("form.html", c=request.form, erros=erros,
                               prioridades=models.PRIORIDADES), 400
    return render_template("form.html", c={}, erros={}, prioridades=models.PRIORIDADES)


@bp.route("/<int:id_>/editar", methods=["GET", "POST"])
def editar(id_):
    chamado = models.obter(id_) or abort(404)
    if request.method == "POST":
        erros = models.validar(request.form)
        if not erros:
            models.atualizar(id_, request.form)
            flash("Chamado atualizado.", "ok")
            return redirect(url_for("chamados.index"))
        return render_template("form.html", c=request.form, erros=erros,
                               prioridades=models.PRIORIDADES), 400
    return render_template("form.html", c=chamado, erros={}, prioridades=models.PRIORIDADES)


@bp.post("/<int:id_>/status")
def status(id_):
    models.obter(id_) or abort(404)
    try:
        models.mudar_status(id_, request.form.get("status"))
        flash("Status alterado.", "ok")
    except ValueError:
        flash("Status inválido.", "erro")
    return redirect(url_for("chamados.index"))


@bp.post("/<int:id_>/excluir")
def excluir(id_):
    models.obter(id_) or abort(404)
    models.excluir(id_)
    flash("Chamado excluído.", "ok")
    return redirect(url_for("chamados.index"))
