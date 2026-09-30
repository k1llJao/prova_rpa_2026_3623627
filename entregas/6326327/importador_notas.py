# =============================================================================
# Questao 4 - Importacao de Notas Fiscais com pandas (Aula 04)
# =============================================================================

import logging

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("importacao.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)


def importar_notas(caminho: str) -> float:
    """Importa notas de um CSV e retorna o total faturado.

    Usa pandas para ler o arquivo e somar a coluna 'valor',
    tratando arquivo inexistente e arquivo vazio.
    """
    total = 0.0
    try:
        df = pd.read_csv(caminho)
        for _, linha in df.iterrows():
            logging.info(
                "Nota %s | Cliente: %s | Valor: R$ %.2f",
                linha["nota"],
                linha["cliente"],
                linha["valor"],
            )
        total = float(df["valor"].sum())
        logging.info("Total faturado: R$ %.2f", total)
        return total
    except FileNotFoundError:
        logging.error("Arquivo nao encontrado: %s", caminho)
        return 0.0
    except pd.errors.EmptyDataError:
        logging.error("Arquivo CSV vazio: %s", caminho)
        return 0.0
    finally:
        logging.info("Tentativa de importacao encerrada para: %s", caminho)


if __name__ == "__main__":
    importar_notas("notas.csv")
    importar_notas("inexistente.csv")
