import mpmath as mp
mp.dps = 15

# Calculate pi/4 directly using mpmath's constant
pi_value = mp.pi
result = pi_value / 4

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))