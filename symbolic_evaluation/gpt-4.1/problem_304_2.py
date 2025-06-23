import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the complete elliptic integral of the first kind K(m) with m = (1/2)^2 = 0.25
k_val = mp.ellipk(0.25)

# Compute the complete elliptic integral of the second kind E(m) with m = 0.25
e_val = mp.ellipe(0.25)

# Calculate the result using the derived expression: 
# (4/3)*K(0.25) - (13/9)*E(0.25)
result = (4/3) * k_val - (13/9) * e_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))