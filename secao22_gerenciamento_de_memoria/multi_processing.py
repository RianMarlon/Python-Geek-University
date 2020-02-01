
from multiprocessing import Pool
import time

CONTADOR = 50000000


def contagem_regressiva(n):

    while n > 0:
        n -= 1


if __name__ == "__main__":
    pool = Pool(processes=2)
    inicio = time.time()
    r1 = pool.apply_async(contagem_regressiva, [CONTADOR // 2])
    r2 = pool.apply_async(contagem_regressiva, [CONTADOR // 2])
    pool.close()
    pool.join()
    fim = time.time()

    print(f"Tempo em segundos: {fim - inicio}")

# Tempo em segundos: 2.525857448577881

