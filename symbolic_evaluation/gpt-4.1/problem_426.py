import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the logarithmic term: (1/2) * ln(6)
log_term = 0.5 * mp.log(6)

# Compute the constant sqrt(3)
sqrt3 = mp.sqrt(3)

# Compute the coefficient for pi: (15 - 4*sqrt3)/24
pi_coeff = (15 - 4 * sqrt3) / 24

# Multiply by pi to get the pi term
pi_term = mp.pi * pi_coeff

# Constant term: -1/4
const_term = -0.25

# Sum all terms to get the final result
result = log_term + pi_term + const_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))