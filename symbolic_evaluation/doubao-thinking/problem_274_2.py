import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the modified Bessel functions of the first kind
I1 = mp.besseli(1, 5)
I3 = mp.besseli(3, 5)

# Calculate the combination 5*I1 - I3
term_combination = 5 * I1 - I3

# Compute the constant coefficient (125 * pi) / 32
coefficient = (125 * mp.pi) / 32

# Multiply coefficient with the Bessel function combination
result = coefficient * term_combination

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))