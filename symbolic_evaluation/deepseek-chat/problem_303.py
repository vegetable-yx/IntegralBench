import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Extract mathematical constant pi
pi_val = mp.pi

# Calculate the fraction: pi divided by 192
result = pi_val / 192

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))