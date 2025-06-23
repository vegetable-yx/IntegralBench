import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Example values for a and b (can be changed by user)
a = 1
b = 1

# Convert to mpmath floats to ensure precision
a_val = mp.mpf(a)
b_val = mp.mpf(b)

# Compute t = (b^2 * a) / 8
t = (b_val**2 * a_val) / 8

# Precompute constant factor: π * √2 * Γ(3/4) * 2^(-1/4)
pi = mp.pi
sqrt_two = mp.sqrt(2)
gamma_three_quarters = mp.gamma(mp.mpf('0.75'))
two_power_neg_quarter = mp.power(2, mp.mpf('-0.25'))
constant_factor = pi * sqrt_two * gamma_three_quarters * two_power_neg_quarter

# Compute (t)^(1/4)
t_power_quarter = mp.power(t, mp.mpf('0.25'))

# Compute exp(t)
exp_t = mp.exp(t)

# Compute Bessel function terms: I_{-1/4}(t) + I_{1/4}(t)
bessel_neg_quarter = mp.besseli(mp.mpf('-0.25'), t)
bessel_quarter = mp.besseli(mp.mpf('0.25'), t)
bessel_sum = bessel_neg_quarter + bessel_quarter

# Combine all factors to get final result
result = constant_factor * t_power_quarter * exp_t * bessel_sum

# Print result to 10 decimal places
print(mp.nstr(result, n=10))