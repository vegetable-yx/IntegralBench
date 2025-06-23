import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute π/4 using exact mathematical operation
result = pi_value / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))