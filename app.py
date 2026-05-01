from flask import Flask, render_template, request

app = Flask(__name__)

CULPADO = "carlos"
PISTAS_NECESSARIAS = {"pegadas", "cameras", "ferramenta"}


def gerar_tabela_verdade(p_jogador, q_jogador, r_jogador, s_jogador):
    """Gera todas as 16 linhas de (P ∧ Q ∧ R) ∧ S."""
    tabela = []
    for bits in range(16):
        p = bool(bits & 0b1000)
        q = bool(bits & 0b0100)
        r = bool(bits & 0b0010)
        s = bool(bits & 0b0001)
        pqr = p and q and r
        resultado = pqr and s
        jogador = (p == p_jogador and q == q_jogador and
                   r == r_jogador and s == s_jogador)
        tabela.append(dict(p=p, q=q, r=r, s=s,
                           pqr=pqr, resultado=resultado, jogador=jogador))
    return tabela


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/jogar", methods=["POST"])
def jogar():
    pegadas    = "pegadas"    in request.form
    cameras    = "cameras"    in request.form
    ferramenta = "ferramenta" in request.form
    suspeito   = request.form.get("suspeito", "")

    tem_todas_pistas = pegadas and cameras and ferramenta
    suspeito_correto = suspeito == CULPADO

    if not tem_todas_pistas:
        nomes = []
        if not pegadas:    nomes.append("Pegadas")
        if not cameras:    nomes.append("Câmera desligada")
        if not ferramenta: nomes.append("Pé de cabra")
        resultado = f"Pistas insuficientes. Ainda falta: {', '.join(nomes)}."
        status = "erro"

    elif not suspeito:
        resultado = "Você tem todas as pistas! Agora identifique o culpado."
        status = "aviso"

    elif suspeito_correto:
        resultado = "CASO ENCERRADO — Carlos foi preso. Excelente trabalho, detetive."
        status = "vitoria"

    else:
        resultado = f"{suspeito.capitalize()} é inocente. Releia as evidências."
        status = "erro"

    tabela = gerar_tabela_verdade(pegadas, cameras, ferramenta, suspeito_correto)

    acertou = status == "vitoria"

    return render_template(
        "resultado.html",
        resultado=resultado,
        status=status,
        acertou=acertou,
        pegadas=pegadas,
        cameras=cameras,
        ferramenta=ferramenta,
        suspeito_correto=suspeito_correto,
        tabela=tabela,
    )


if __name__ == "__main__":
    app.run(debug=True)