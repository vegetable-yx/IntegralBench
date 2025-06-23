import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the value of pi
pi_value = mp.pi

# Divide pi by 4 to get the result
result = pi_value / 4

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))