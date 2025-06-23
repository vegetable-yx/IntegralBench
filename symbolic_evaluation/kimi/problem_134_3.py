import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute π using mpmath constant
pi_value = mp.pi

# Compute square root of 2
sqrt_two = mp.sqrt(2)

# Calculate the final result by multiplying π and sqrt(2)
result = pi_value * sqrt_two

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))