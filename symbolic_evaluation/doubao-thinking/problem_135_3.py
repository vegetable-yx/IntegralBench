import mpmath as mp

# Set decimal places for internal calculations to 15
mp.dps = 15

# Calculate the constant pi
pi_value = mp.pi

# Multiply pi by 3
three_pi = 3 * pi_value

# Divide the result by 4
result = three_pi / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))