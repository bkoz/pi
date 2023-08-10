from random import random
import time

N = 10000000  # the experiment event number
r = 1  # the circle radius
n = 0  # sucessful event number

t0 = time.time()
r2 = r * r
for i in range(N):
    x = -r + 2 * r * random()
    y = -r + 2 * r * random()

    #
    # If the random point is inside the circle, increment n.
    #
    if ((x * x + y * y) <= r2):
        n = n + 1

pi_sim = 4 * n / N
elapsed_time = time.time() - t0
print(f'Pi = {pi_sim:.7f}')
print(f'Elasped time = {elapsed_time:.3f} secs.')
