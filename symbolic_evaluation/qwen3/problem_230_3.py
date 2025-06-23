import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate pi to the fourth power
pi_4 = mp.power(mp.pi, 4)

# Divide by 160 to get the result
result = pi_4 / 160

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))