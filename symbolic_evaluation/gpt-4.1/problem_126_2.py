import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the complete elliptic integral of the first kind at k = 1/2
k_value = mp.mpf(1)/mp.mpf(2)
elliptic_k = mp.ellipk(k_value)

# Multiply by pi/2
result = (mp.pi / 2) * elliptic_k

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))