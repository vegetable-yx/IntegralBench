import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the Bessel function of the first kind of order 1 at x=1
j1_val = mp.besselj(1, 1)

# Multiply by π to get the final result
result = mp.pi * j1_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))