import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate pi^4 using mpmath's constant
pi_power4 = mp.pi ** 4

# Divide by 480 to get the final result
result = pi_power4 / 480

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))