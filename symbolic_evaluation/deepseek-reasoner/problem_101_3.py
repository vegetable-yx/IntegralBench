import mpmath as mp
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Divide pi by 32 to get the result
result = pi_value / 32

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))