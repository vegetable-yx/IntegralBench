import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute pi^4 by squaring pi^2
pi_squared = mp.power(pi_value, 2)
pi_fourth = mp.power(pi_squared, 2)

# Divide pi^4 by 32 to get final result
result = mp.fdiv(pi_fourth, 32)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))