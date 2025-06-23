import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute fundamental constants
pi = mp.pi
sqrt_pi = mp.sqrt(pi)
sqrt2 = mp.sqrt(2)

# Precompute trigonometric constants for pi/8 (22.5 degrees)
cos_pi8 = mp.cos(pi/8)
sin_pi8 = mp.sin(pi/8)

# Compute the digamma function at 1/2
digamma_half = mp.digamma(0.5)

# Compute logarithmic terms
ln2 = mp.ln(2)
# Compute ln((√2+1)/(√2-1)) using direct ratio calculation
log_arg = (sqrt2 + 1) / (sqrt2 - 1)
ln_term = mp.ln(log_arg)

# Combine components inside the brackets
term1 = digamma_half
term2 = 0.5 * ln2
term3 = (sqrt2 / 2) * ln_term
bracket_sum = term1 + term2 + term3

# Compute the main expression inside braces
inner_part = cos_pi8 * bracket_sum
outer_part = (pi/4) * sin_pi8
braces = inner_part - outer_part

# Compute the prefactor: √π / 2^(1/4)
prefactor = sqrt_pi / (2**(0.25))

# Final result
result = prefactor * braces

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))