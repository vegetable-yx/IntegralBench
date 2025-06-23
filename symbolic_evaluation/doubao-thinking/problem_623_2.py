import mpmath as mp

# Set internal precision to 15 decimal places for calculations
mp.dps = 15

# Compute arcsin(1/3) using mpmath's asin function
asin_val = mp.asin(mp.mpf(1)/3)

# Multiply the result by pi
result = mp.pi * asin_val

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))