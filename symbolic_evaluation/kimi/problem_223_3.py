import mpmath as mp
mp.dps = 15

# Calculate pi squared using mpmath's constant for pi
pi_value = mp.pi
result = pi_value ** 2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))