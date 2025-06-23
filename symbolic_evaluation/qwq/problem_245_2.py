import mpmath as mp
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi raised to the 4th power
pi_power4 = pi_val**4

# Multiply by 3
three_pi4 = 3 * pi_power4

# Divide by 2 to get the final result
result = three_pi4 / 2

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))