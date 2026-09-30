# =============================================================================
# Questao 2 - Monitoramento de Sensores e Controle de Fluxo (Aula 02)
# =============================================================================

leituras = [36.5, 41.2, 38.0, 105.0, 37.4, -999.0, 39.1, 40.0]


def monitorar(lista):
    """Processa a fila de leituras conforme as regras do enunciado."""
    validas = []

    for leitura in lista:
        if leitura == -999.0:
            print("[FALHA] Sensor corrompido — processamento interrompido.")
            break
        if leitura > 80.0:
            print(f"[DESCARTE] {leitura}C fora da faixa — ignorado.")
            continue
        print(f"[OK] Leitura de {leitura}C registrada.")
        validas.append(leitura)
    else:
        if validas:
            media = sum(validas) / len(validas)
        else:
            media = 0.0
        print(f"\nQuantidade de leituras validas: {len(validas)}")
        print(f"Media: {media:.2f}C")


if __name__ == "__main__":
    monitorar(leituras)
