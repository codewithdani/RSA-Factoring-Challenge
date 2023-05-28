import sys

def factorize_number(n):
    factors = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors

# Check if the script is called with the filename argument
if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        for line in file:
            number = int(line.strip())
            factorizations = factorize_number(number)
            for factorization in factorizations:
                p, q = factorization
                print(f"{number}={p}*{q}")
except FileNotFoundError:
    print(f"File '{filename}' not found.")
    sys.exit(1)
