#!/usr/bin/env python3
"""
Rodador de soluções OBI
------------------------
Roda seu programa (Python, C, C++, Java, Pascal ou Javascript) usando o
conteúdo de um arquivo .txt como entrada padrão (stdin), e mostra a saída.

Por padrão, a entrada é lida do arquivo "inputQuestao.txt" (na pasta atual).

USO:
    python rodar_obi.py <arquivo_solucao>
    python rodar_obi.py <arquivo_solucao> --entrada outro_arquivo.txt

EXEMPLOS:
    python rodar_obi.py media.py
    python rodar_obi.py media.cpp --entrada entrada1.txt
    python rodar_obi.py passatempo.java --entrada entrada1.txt

Também dá para testar VÁRIOS exemplos de uma vez, se você organizar assim:
    testes/
        1.in
        2.in
        ...
    python rodar_obi.py media.py --entrada testes/
(o script detecta os arquivos *.in automaticamente dentro da pasta)
"""

import os
import sys
import subprocess
import tempfile
import glob
import argparse


# =====================================================================
# CONFIGURAÇÃO DOS ARGUMENTOS (fica logo no topo, antes de qualquer
# outra parte do código, para ficar fácil de achar e mexer)
# =====================================================================
parser = argparse.ArgumentParser(
    description="Roda uma solução OBI usando um arquivo .txt como entrada padrão.",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=__doc__,
)

parser.add_argument(
    "solucao",
    help="Arquivo com o código-fonte (ex: media.py, media.cpp)",
)

parser.add_argument(
    "--entrada",
    default="inputQuestao.txt",
    help="Arquivo de entrada (ou pasta com arquivos *.in). Padrão: inputQuestao.txt",
)

parser.add_argument(
    "--timeout",
    type=int,
    default=10,
    help="Tempo máximo (em segundos) que o programa pode rodar. Padrão: 10",
)

args = parser.parse_args()
# =====================================================================
# FIM DA CONFIGURAÇÃO DOS ARGUMENTOS
# =====================================================================


def compilar_se_preciso(caminho_fonte):
    """Compila o código se necessário e devolve o comando para executá-lo."""
    ext = os.path.splitext(caminho_fonte)[1].lower()
    nome_base = os.path.splitext(os.path.basename(caminho_fonte))[0]
    pasta_tmp = tempfile.mkdtemp(prefix="obi_")

    if ext == ".py":
        return [sys.executable, caminho_fonte]

    if ext == ".js":
        return ["node", caminho_fonte]

    if ext in (".c", ".cpp", ".cc"):
        exe = os.path.join(pasta_tmp, nome_base + (".exe" if os.name == "nt" else ""))
        compilador = "gcc" if ext == ".c" else "g++"
        cmd_compilacao = [compilador, caminho_fonte, "-O2", "-o", exe]
        r = subprocess.run(cmd_compilacao, capture_output=True, text=True)
        if r.returncode != 0:
            print("ERRO AO COMPILAR:\n", r.stderr)
            raise SystemExit(1)
        return [exe]

    if ext == ".pas":
        exe = os.path.join(pasta_tmp, nome_base)
        r = subprocess.run(["fpc", "-o" + exe, caminho_fonte], capture_output=True, text=True)
        if r.returncode != 0:
            print("ERRO AO COMPILAR:\n", r.stdout, r.stderr)
            raise SystemExit(1)
        return [exe]

    if ext == ".java":
        pasta_fonte = os.path.dirname(os.path.abspath(caminho_fonte)) or "."
        r = subprocess.run(["javac", caminho_fonte], capture_output=True, text=True, cwd=pasta_fonte)
        if r.returncode != 0:
            print("ERRO AO COMPILAR:\n", r.stderr)
            raise SystemExit(1)
        return ["java", "-cp", pasta_fonte, nome_base]

    print(f"Extensão '{ext}' não suportada. Use .py, .c, .cpp, .cc, .java, .pas ou .js")
    raise SystemExit(1)


def rodar_um_teste(cmd, arquivo_entrada):
    with open(arquivo_entrada, "r") as f_in:
        entrada = f_in.read()

    try:
        resultado = subprocess.run(
            cmd, input=entrada, capture_output=True, text=True, timeout=args.timeout
        )
    except subprocess.TimeoutExpired:
        print(f"[{arquivo_entrada}] TIMEOUT (mais de {args.timeout}s)")
        return

    saida_obtida = resultado.stdout

    if resultado.returncode != 0:
        print(f"[{arquivo_entrada}] O programa terminou com erro (código {resultado.returncode}):")
        print(resultado.stderr)
        return

    print(f"--- Entrada: {arquivo_entrada} ---")
    print("Saída do seu programa:")
    print(saida_obtida.rstrip("\n"))
    print()


def main():
    cmd = compilar_se_preciso(args.solucao)

    # Modo pasta: roda todos os arquivos *.in dentro dela
    if os.path.isdir(args.entrada):
        arquivos_in = sorted(glob.glob(os.path.join(args.entrada, "*.in")))
        if not arquivos_in:
            print("Nenhum arquivo .in encontrado na pasta.")
            raise SystemExit(1)
        for arq_in in arquivos_in:
            rodar_um_teste(cmd, arq_in)
    else:
        rodar_um_teste(cmd, args.entrada)


if __name__ == "__main__":
    main()