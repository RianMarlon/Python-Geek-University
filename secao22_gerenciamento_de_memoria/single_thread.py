
import time

CONTADOR = 50000000


def contagem_regressiva(n):

    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f"Tempo em segundos: {fim - inicio}")

# Tempo em segundos: 4.041193962097168


