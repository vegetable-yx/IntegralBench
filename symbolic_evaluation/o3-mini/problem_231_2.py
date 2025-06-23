import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant 2 as an mpmath floating-point number
base_value = mp.mpf(2)

# Compute the square root of the base value
result = mp.sqrt(base_value)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))