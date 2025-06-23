import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the complete elliptic integral of the first kind K(1/2)
k_value = mp.mpf(1)/mp.mpf(2)
K = mp.ellipk(k_value)

# Multiply by 2 to get the final result
result = 2 * K

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))