import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi cubed (π^3)
pi_cubed = mp.pi ** 3

# Multiply by 7: 7 * π^3
numerator = 7 * pi_cubed

# Divide by 64 to get the final result
result = numerator / 64

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))