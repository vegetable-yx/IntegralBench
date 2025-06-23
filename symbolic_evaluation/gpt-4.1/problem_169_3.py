import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter for the elliptic integral
k_val = 0.5

# Compute the complete elliptic integral of the first kind K(k)
K = mp.ellipk(k_val)

# Multiply by π/2 as per the expression
result = (mp.pi / 2) * K

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))