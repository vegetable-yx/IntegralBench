import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the exact value of pi
pi_value = mp.pi

# Divide pi by 2 to obtain the result
result = pi_value / 2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))