import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate 2 raised to the power of 5/4
two_power = mp.power(2, 5/4)

# Calculate pi raised to the power of 3/2
pi_power = mp.power(mp.pi, 3/2)

# Multiply the two components
result = two_power * pi_power

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))