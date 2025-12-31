from time import perf_counter
from math import sqrt
import os

os.system('clear')

primes = [2]
counter_brute_force = 10**4
current = 3
start= perf_counter()

print("Brute force iteration")
print("-------------------------------")
print("-------------------------------")

while len(primes) < counter_brute_force:
    is_prime = True
    for p in primes : 
        if current % p == 0:
            is_prime = False
            break
    if is_prime:
        #print(current)
        primes.append(current)
    current += 2 

print(primes[:100])
print(primes[-100:])

stop = perf_counter()
print(f"It took: {stop-start:.2f}s. iterating {counter_brute_force} times")

print("-------------------------------")
print("-------------------------------")

print("Aritostenes sieve iteration")
print("-------------------------------")
print("-------------------------------")

primes_aritostenes = [2]
counter_aritostenes = 10**4
current_aritostenes = 3
start_aritostenes= perf_counter()


while len(primes_aritostenes) < counter_aritostenes:
    is_prime = True
    current_sqrt = int(sqrt(current_aritostenes)) + 1
    for p in primes_aritostenes: 
        if p > current_sqrt:
            break
        if current_aritostenes % p == 0:
            is_prime = False
            break
    if is_prime:
        #print(current_aritostenes)
        primes_aritostenes.append(current_aritostenes)
    current_aritostenes += 2 

print(primes_aritostenes[:100])
print(primes_aritostenes[-100:])

stop_aritostenes = perf_counter()
print(f"It took: {stop_aritostenes-start_aritostenes:.2f}s. iterating {counter_aritostenes} times")

print("-------------------------------")
print("-------------------------------")

print("Aritostenes sieve iteration optimized ")
print("-------------------------------")
print("-------------------------------")

primes_aritostenes = [2,3]
counter_aritostenes = 10**4
start_aritostenes= perf_counter()

k = 6

while len(primes_aritostenes) < counter_aritostenes:
    a = k - 1
    b = k + 1
    current_sqrt = int(sqrt(b)) + 1 
    for current_aritostenes in [a,b]:
        is_prime = True
        for p in primes_aritostenes: 
            if p > current_sqrt:
                break
            if current_aritostenes % p == 0:
                is_prime = False
                break
        if is_prime:
            #print(current_aritostenes)
            primes_aritostenes.append(current_aritostenes)
        k += 6

print(primes_aritostenes[:100])
print(primes_aritostenes[-100:])

stop_aritostenes = perf_counter()
print(f"It took: {stop_aritostenes-start_aritostenes:.2f}s. iterating {counter_aritostenes} times")
