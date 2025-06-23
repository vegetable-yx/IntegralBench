import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi to the fourth power
pi_4 = mp.power(mp.pi, 4)

# Multiply by 7
numerator = 7 * pi_4

# Divide by 30 to get final result
result = numerator / 30

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))