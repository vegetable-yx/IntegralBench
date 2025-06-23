import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the numerator: 1 + sqrt(2)
numerator = 1 + sqrt2

# Divide by 2 to form the argument for the logarithm
arg = numerator / 2

# Compute the natural logarithm of the argument
log_val = mp.log(arg)

# Multiply by pi to get the final result
result = mp.pi * log_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))