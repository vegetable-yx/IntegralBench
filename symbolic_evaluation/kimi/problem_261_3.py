import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate Bessel function of the first kind of order 1 at 2
j1_2 = mp.besselj(1, 2)

# Multiply by π and divide by 4
result = (mp.pi * j1_2) / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))