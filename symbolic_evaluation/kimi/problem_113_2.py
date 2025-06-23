import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate pi^3
pi_cubed = mp.pi ** 3

# Calculate square root of 2
sqrt_two = mp.sqrt(2)

# Multiply pi^3 by sqrt(2)
numerator = pi_cubed * sqrt_two

# Divide by 6 to get the result
result = numerator / 6

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))