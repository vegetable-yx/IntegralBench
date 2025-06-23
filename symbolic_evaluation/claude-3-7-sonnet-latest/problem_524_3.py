import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute e^2
e_squared = mp.power(mp.e, 2)

# Add 1 to e^2
numerator = mp.fadd(e_squared, 1)

# Divide the numerator by 4
result = mp.fdiv(numerator, 4)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))