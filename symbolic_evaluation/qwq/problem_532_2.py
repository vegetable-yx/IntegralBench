import mpmath as mp
mp.dps = 15

# Calculate pi squared using mpmath's constant
pi_squared = mp.pi ** 2

# Set final result and print with 10 decimal precision
result = pi_squared
print(mp.nstr(result, n=10))