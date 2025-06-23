import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
root_two = mp.sqrt(2)

# Multiply by 2 to get the final result
result = 2 * root_two

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))