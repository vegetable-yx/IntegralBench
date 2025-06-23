import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute gamma(1/4)
gamma_val = mp.gamma(0.25)

# Raise gamma(1/4) to the fourth power
gamma_fourth = gamma_val**4

# Compute the denominator: 128 * pi
denominator = 128 * mp.pi

# Divide the numerator (gamma_fourth) by the denominator
result = gamma_fourth / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))