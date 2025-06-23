import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute each term separately for clarity and precision
# Term 1: Constant 1
term1 = mp.mpf(1)

# Term 2: -√2 / 2
sqrt2 = mp.sqrt(2)  # Compute square root of 2
term2 = -sqrt2 / 2  # Divide by 2 and negate

# Term 3: (1/2) * ln(2)
ln2 = mp.log(2)     # Natural logarithm of 2
term3 = 0.5 * ln2   # Multiply by 1/2

# Sum all terms to get final result
result = term1 + term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))