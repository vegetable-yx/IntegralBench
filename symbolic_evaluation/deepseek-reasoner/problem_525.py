import mpmath as mp
mp.dps = 15  # Set decimal places for internal precision

# Compute the exact value of 1/2 using high-precision arithmetic
result = mp.mpf(1)/2

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))