import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate Bessel function of the first kind of order 2 at 1
j2_value = mp.besselj(2, 1)

# Multiply by pi constant to get the final result
result = mp.pi * j2_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))