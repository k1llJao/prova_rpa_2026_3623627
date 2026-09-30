# =============================================================================
# Questao 3 - Integracao (Aula 03)
# =============================================================================

from mod_estoque import (
    cadastrar_item,
    calcular_valor_estoque,
    listar_itens_em_falta,
)


def main():
    """Ponto de entrada da Questao 3."""
    itens = [
        cadastrar_item("Parafuso M6", 200, 0.35),
        cadastrar_item("Porca M6", 15, 0.20),
        cadastrar_item("Arruela", 4, 0.10),
    ]

    valor_total = calcular_valor_estoque(itens)
    print(f"Valor total do estoque: R$ {valor_total:.2f}")

    minimo = 20
    em_falta = listar_itens_em_falta(itens, minimo)
    print(f"\nItens com quantidade abaixo de {minimo}:")
    if em_falta:
        for item in em_falta:
            print(
                f"  - {item['nome']}: "
                f"{item['quantidade']} unidades"
            )
    else:
        print("  Nenhum item em falta.")


if __name__ == "__main__":
    main()
