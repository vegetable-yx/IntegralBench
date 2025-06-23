import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the argument for sine function
x = mp.mpf(1)

# Compute sin(1) using mpmath sine function
result = mp.sin(x)

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))