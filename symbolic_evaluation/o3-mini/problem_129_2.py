import mpmath as mp

# Set the internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the exponential term: e^(1/2)
exp_term = mp.exp(0.5)

# Calculate the modified Bessel function of the second kind at order 1/4 and argument 1/2
bessel_term = mp.besselk(0.25, 0.5)

# Calculate the numerator: 2 * e^(1/2) * K_{1/4}(1/2)
numerator = 2 * exp_term * bessel_term

# Calculate the denominator: sqrt(pi)
denominator = mp.sqrt(mp.pi)

# Compute the final result: numerator / denominator
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))