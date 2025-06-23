import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi^4 using mpmath's constant
pi_squared = mp.pi ** 2
pi_power4 = pi_squared ** 2

# Divide the result by 32
result = pi_power4 / 32

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))