import mpmath as mp

# Set the decimal places for internal precision
mp.dps = 15

# Compute gamma(1/4)
gamma_val = mp.gamma(0.25)

# Raise gamma(1/4) to the 8th power
gamma_eighth = gamma_val**8

# Calculate the denominator: 512 * pi^2
pi_sq = mp.pi**2
denominator = 512 * pi_sq

# Prefactor: gamma(1/4)^8 / (512 * pi^2)
prefactor = gamma_eighth / denominator

# Compute the generalized hypergeometric function 3F2
# Arguments: a = [1/4, 1/4, 1/4], b = [1/2, 3/4], z = 1/16
hyper_val = mp.hyper3f2(0.25, 0.25, 0.25, 0.5, 0.75, 1/16)

# Multiply the prefactor by the hypergeometric function
result = prefactor * hyper_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))