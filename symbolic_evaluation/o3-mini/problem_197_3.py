import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the analytical expression: 1/4
# This is a simple fraction that can be computed directly
numerator = mp.mpf(1)   # Convert integer 1 to mpmath float
denominator = mp.mpf(4) # Convert integer 4 to mpmath float
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))