import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(1/4)

# Raise to the 4th power
gamma_fourth = gamma_val**4

# Divide by 16
result = gamma_fourth / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))