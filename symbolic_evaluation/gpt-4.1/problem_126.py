import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the complete elliptic integral of the second kind for k=0.5
E_value = mp.ellipe(0.5)

# Multiply by pi to get the final result
result = mp.pi * E_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))