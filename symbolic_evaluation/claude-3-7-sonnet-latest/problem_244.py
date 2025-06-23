import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi to the fourth power
pi_4 = mp.power(mp.pi, 4)

# Multiply by 3
numerator = 3 * pi_4

# Divide by 32 to get the final result
result = numerator / 32

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))