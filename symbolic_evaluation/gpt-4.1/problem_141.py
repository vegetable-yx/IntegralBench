import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Example value for parameter 'a' (can be changed by user)
a = 1.0

# Compute modified Bessel function I_1(a)
bessel_term = mp.besseli(1, a)

# Compute first term: π * I_1(a) / a
term1 = (mp.pi / a) * bessel_term

# Compute hyperbolic sine sinh(a)
sinh_val = mp.sinh(a)

# Compute second term: 2 * sinh(a) / a^2
term2 = (2 * sinh_val) / (a**2)

# Combine terms: result = term1 - term2
result = term1 - term2

# Print final result with 10 decimal places
print(mp.nstr(result, n=10))