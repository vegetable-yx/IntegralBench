import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the value of pi
pi_value = mp.pi

# Divide pi by 8 to get the result
result = pi_value / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))