CREATE TABLE IF NOT EXISTS chamado (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo      VARCHAR(100) NOT NULL CHECK (length(trim(titulo)) BETWEEN 1 AND 100),
    descricao   TEXT NOT NULL CHECK (length(trim(descricao)) BETWEEN 1 AND 2000),
    solicitante VARCHAR(80) NOT NULL CHECK (length(trim(solicitante)) BETWEEN 1 AND 80),
    prioridade  VARCHAR(10) NOT NULL CHECK (prioridade IN ('baixa','media','alta')),
    status      VARCHAR(15) NOT NULL DEFAULT 'aberto'
                CHECK (status IN ('aberto','em_andamento','resolvido')),
    criado_em   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
