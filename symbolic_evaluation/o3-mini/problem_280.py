import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define variables a and b (example values, can be modified)
a = 1.0
b = 1.0

# Calculate constant factor: sqrt(pi) * Gamma(3/4) / (sqrt(2) * Gamma(5/4))
const_num = mp.sqrt(mp.pi) * mp.gamma(3/4)
const_den = mp.sqrt(2) * mp.gamma(5/4)
const_factor = const_num / const_den

# Compute argument for Bessel function and power term: ab/2
arg = (a * b) / 2

# Compute a^{1/2}
a_power = mp.sqrt(a)

# Compute (ab/2)^{-1/4}
ab_power = arg ** (-1/4)

# Compute modified Bessel function of the first kind: I_{1/4}(ab/2)
bessel_term = mp.besseli(0.25, arg)  # 1/4 = 0.25

# Combine all terms to get final result
result = const_factor * a_power * ab_power * bessel_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))