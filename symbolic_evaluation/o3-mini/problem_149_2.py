import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the hypergeometric function term
# Using mp.hyper for the generalized hypergeometric function {}_3F_2
# Arguments: top parameters [1/2, 1/2, 1/2], bottom parameters [1, 1], and z=1/2
hyper_term = mp.hyper([mp.mpf('0.5'), mp.mpf('0.5'), mp.mpf('0.5')], 
                      [1, 1], 
                      mp.mpf('0.5'))

# Compute the constant factor: (π² * √2) / 2
pi_sq = mp.pi ** 2
sqrt2 = mp.sqrt(2)
constant_factor = (pi_sq * sqrt2) / 2

# Multiply the hypergeometric term by the constant factor
result = constant_factor * hyper_term

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))