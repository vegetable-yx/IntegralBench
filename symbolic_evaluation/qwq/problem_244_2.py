import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate π^4 using mpmath's pi
pi_power4 = mp.power(mp.pi, 4)

# Multiply by 3 to get the numerator
numerator = 3 * pi_power4

# Divide by 128 to get the final result
result = mp.fdiv(numerator, 128)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))