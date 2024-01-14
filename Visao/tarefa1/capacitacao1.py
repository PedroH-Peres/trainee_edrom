# Pedro Henrique Bohling Peres
# Tarefa 1 - Visão EDROM

import os

if not os.path.exists("completes"):
    os.mkdir("completes")

for arq in os.listdir("labels"):
    cur = open(f"labels/{str(arq)}", "r")

    txt = cur.read()
    txt = txt.replace("0", "1", 1)
    cur.close()

    cur = open(f"labels/{str(arq)}", "w")
    cur.write(txt)
    cur.close()
    os.rename(f"labels/{str(arq)}", f"completes/computer{arq[len(arq)-5]}")

