import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the value of pi
pi_value = mp.pi

# Divide pi by 4 to get the result
result = pi_value / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))