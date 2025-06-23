import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Bessel function of the first kind of order 1 at 1
j1_value = mp.besselj(1, 1)

# Multiply by pi to get the final result
result = mp.pi * j1_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))