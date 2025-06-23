import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Example values for a and b (modify as needed)
a = 1.0
b = 1.0

# Compute Gamma(1/4) and square it
gamma_1_4 = mp.gamma(mp.mpf('1/4'))
gamma_squared = gamma_1_4 ** 2

# Compute denominator sqrt(π*a)
sqrt_pi_a = mp.sqrt(mp.pi * a)

# Compute hypergeometric function 1F2 parameters and argument
hyper_arg = (a**2 * b**2) / 16
hyper_term = mp.hyper([mp.mpf('1/4')], [mp.mpf('1/2'), mp.mpf('3/4')], hyper_arg)

# Combine all components for final result
result = (gamma_squared / sqrt_pi_a) * hyper_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))