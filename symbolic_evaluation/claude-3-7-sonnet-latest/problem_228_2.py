import mpmath as mp

# Set internal precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate pi raised to the 5th power
pi_power5 = mp.pi ** 5

# Multiply by 7 to get the numerator
numerator = 7 * pi_power5

# Divide the numerator by 144
fraction = numerator / 144

# Apply the negative sign to get the final result
result = -fraction

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))