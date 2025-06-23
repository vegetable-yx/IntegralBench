import mpmath as mp

# Set internal decimal places for precision (15 to ensure 10 decimal places accuracy)
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(1/4)

# Raise Gamma(1/4) to the 4th power
gamma_power = gamma_val ** 4

# Divide the result by 64
result = gamma_power / 64

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))