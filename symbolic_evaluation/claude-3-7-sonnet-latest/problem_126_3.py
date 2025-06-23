import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute the complete elliptic integral of the first kind at k=0.5
k_val = mp.ellipk(0.5)

# Multiply by 2π to get the final result
result = 2 * mp.pi * k_val

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))