import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute each term of the expression separately
# Term 1: π²/6
term1 = (mp.pi ** 2) / 6

# Term 2: π multiplied by square root of 3
term2 = mp.pi * mp.sqrt(3)

# Term 3: -2π
term3 = -2 * mp.pi

# Sum all terms to get the result
result = term1 + term2 + term3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))