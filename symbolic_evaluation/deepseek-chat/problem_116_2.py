import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(1/4)

# Raise Gamma(1/4) to the 4th power
gamma_fourth = gamma_val**4

# Divide by 32
result = gamma_fourth / 32

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))