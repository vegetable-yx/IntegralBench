import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Define parameters for the hypergeometric function
numer_params = [mp.mpf('0.5'), mp.mpf('0.5'), mp.mpf(1)]
denom_params = [mp.mpf('1.5'), mp.mpf('1.5'), mp.mpf('1.5')]
z = mp.mpf('-0.25')

# Calculate the generalized hypergeometric function 3F3
hyper_term = mp.hyper(numer_params, denom_params, z)

# Calculate the coefficient sqrt(pi)/2
sqrt_pi = mp.sqrt(mp.pi)
coefficient = sqrt_pi / 2

# Combine components for final result
result = coefficient * hyper_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))