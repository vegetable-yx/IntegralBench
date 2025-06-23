import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Bessel function of the first kind of order 1 at x=2
j1_val = mp.besselj(1, 2)

# Multiply by π and divide by 4 to get the result
result = (mp.pi * j1_val) / 4

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))