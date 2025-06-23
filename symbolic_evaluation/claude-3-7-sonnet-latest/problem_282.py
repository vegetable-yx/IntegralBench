import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters a and b (example values, can be modified)
a_val = mp.mpf('1.0')
b_val = mp.mpf('1.0')

# Step 1: Compute Gamma(1/4)
gamma_quarter = mp.gamma(mp.mpf('0.25'))

# Step 2: Square the Gamma(1/4) value
gamma_sq = gamma_quarter ** 2

# Step 3: Compute a^{-1/2}
a_power = 1 / mp.sqrt(a_val)

# Step 4: Compute the argument for the Bessel function: (b * a) / 2
bessel_arg = (b_val * a_val) / 2

# Step 5: Compute the modified Bessel function of the first kind, order 0
bessel_i0 = mp.besseli(0, bessel_arg)

# Step 6: Compute the constant factor: Gamma(1/4)^2 / pi
constant_factor = gamma_sq / mp.pi

# Step 7: Combine all parts: constant_factor * a_power * bessel_i0
result = constant_factor * a_power * bessel_i0

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))