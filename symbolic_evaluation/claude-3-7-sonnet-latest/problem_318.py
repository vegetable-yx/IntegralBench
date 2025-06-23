import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of variable 'a' (here we set a=1 for computation)
a_val = mp.mpf(1)

# Compute the denominator: pi times a squared
denominator = mp.pi * a_val**2

# Calculate the result: 2 divided by (pi * a^2)
result = mp.mpf(2) / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))