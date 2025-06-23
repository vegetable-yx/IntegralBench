import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the exact value of pi
pi_value = mp.pi

# Divide pi by 3 to get the result
result = pi_value / 3

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))