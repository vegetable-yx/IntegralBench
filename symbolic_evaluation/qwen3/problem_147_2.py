import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi**2

# Calculate the square root of 2
sqrt_two = mp.sqrt(2)

# Divide pi squared by sqrt(2)
result = pi_squared / sqrt_two

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))