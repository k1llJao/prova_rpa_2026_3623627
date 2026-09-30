# =============================================================================
# Questao 1 - Parametros de Conexao e Tipagem (Aula 01)
# =============================================================================

ENDPOINT_URL: str = "https://api.exemplo.com"
PORTA: int = 8443
TAXA_AMOSTRAGEM: float = 0.5
USA_HTTPS: bool = True

parametros = {
    "ENDPOINT_URL": ENDPOINT_URL,
    "PORTA": PORTA,
    "TAXA_AMOSTRAGEM": TAXA_AMOSTRAGEM,
    "USA_HTTPS": USA_HTTPS,
}


def main():
    """Ponto de entrada da Questao 1."""
    print("=== Relatorio de Validacao de Parametros ===")
    for nome, valor in parametros.items():
        print(f"{nome}: valor = {valor!r}, tipo = {type(valor)}")


if __name__ == "__main__":
    main()
