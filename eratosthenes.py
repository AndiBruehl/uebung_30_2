import time

print()
print("Das Sieb des Eratosthenes")
print("=========================")
print()

def eratosthenes_sieve(n):
    primes = [True] * (n+1)
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1
    prim_list = [str(p) for p in range(2, n+1) if primes[p]]
    prim_str = ", ".join(prim_list)
    with open("prim.txt", "w") as f:
        f.write(prim_str)
    print("Die Primzahlen bis zur Obergrenze", n, "sind:", prim_str)

upper_limit = int(input("Geben Sie die Obergrenze ein: "))
print()
start = time.time()
eratosthenes_sieve(upper_limit)
end = time.time()
print()
print("Time taken:", end - start, "seconds.")
print()
print("Programmende")
print()
input("Zum beenden beliebige Taste drücken.")