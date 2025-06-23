import mpmath as mp
mp.dps = 15

# Calculate pi squared using mpmath's constant
pi_squared = mp.pi ** 2

# Divide by 32 to obtain the final result
result = pi_squared / 32

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))