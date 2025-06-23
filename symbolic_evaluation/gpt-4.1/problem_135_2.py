import mpmath as mp

# Set internal decimal precision to 15 digits for calculations
mp.dps = 15

# Calculate the constant pi using mpmath
pi_val = mp.pi

# Multiply pi by 3
numerator = 3 * pi_val

# Divide the result by 4 to get the final value
result = numerator / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))