#!/usr/bin/env python
import time
import sys

from CalculaCPF import CalculaCPF

def main():
    start_time = time.time()

    saida = sys.stdout
    buffersize=100000
    f = open('CPFs.txt', 'w', buffering=buffersize)
    sys.stdout = f
    for y in range(0, 1000000000):
        new = str(f'{y:09}')
        print(CalculaCPF(new))

    sys.stdout = saida
    f.close()

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()
