import pytest
from app import create_app, models

VALIDO = {"titulo": "VPN caiu", "descricao": "Sem acesso", "solicitante": "Ana", "prioridade": "alta"}


@pytest.fixture
def client(tmp_path):
    app = create_app(str(tmp_path / "t.db"))
    app.config["TESTING"] = True
    return app, app.test_client()


# --- testes unitários do Model (verificação) ---
def test_validar_ok():
    assert models.validar(VALIDO) == {}


def test_validar_campos_invalidos():
    erros = models.validar({"titulo": " ", "descricao": "", "solicitante": "", "prioridade": "x"})
    assert set(erros) == {"titulo", "descricao", "solicitante", "prioridade"}


def test_crud_model(client):
    app, _ = client
    with app.app_context():
        id_ = models.criar(VALIDO)
        assert models.obter(id_)["status"] == "aberto"
        models.mudar_status(id_, "resolvido")
        assert models.listar("resolvido")[0]["id"] == id_
        with pytest.raises(ValueError):
            models.mudar_status(id_, "inexistente")
        models.excluir(id_)
        assert models.obter(id_) is None


# --- testes de integração via HTTP (validação) ---
def test_criar_via_http(client):
    _, c = client
    r = c.post("/novo", data=VALIDO, follow_redirects=True)
    assert r.status_code == 200 and b"VPN caiu" in r.data


def test_erro_tratado_no_formulario(client):
    _, c = client
    r = c.post("/novo", data={**VALIDO, "titulo": ""})
    assert r.status_code == 400 and "Informe um título".encode() in r.data


def test_404(client):
    _, c = client
    assert c.get("/999/editar").status_code == 404


def test_fluxo_status_e_exclusao(client):
    _, c = client
    c.post("/novo", data=VALIDO)
    c.post("/1/status", data={"status": "em_andamento"})
    assert b"em andamento" in c.get("/?status=em_andamento").data
    c.post("/1/excluir")
    assert b"Nenhum chamado" in c.get("/").data


@pytest.mark.parametrize("descricao", ["x" * 2001, "   ", ""])
def test_limite_descricao(descricao):
    assert "descricao" in models.validar({**VALIDO, "descricao": descricao})

def test_descricao_no_limite():
    assert models.validar({**VALIDO, "descricao": "x" * 2000}) == {}

def test_banco_recusa_descricao_longa(client):
    import sqlite3
    app, _ = client
    with app.app_context():
        with pytest.raises(sqlite3.IntegrityError):
            models.criar({**VALIDO, "descricao": "x" * 2001})

def test_http_recusa_descricao_longa(client):
    _, c = client
    r = c.post("/novo", data={**VALIDO, "descricao": "x" * 2001})
    assert r.status_code == 400
