import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (user should modify these values as needed)
a = 1.0  # Example value, can be changed
b = 1.0  # Example value, can be changed

# Compute common argument for Bessel functions
arg = (a * b) / 4

# Compute modified Bessel functions of the first kind
I_minus = mp.besseli(-1/4, arg)  # I_{-1/4}(ab/4)
I_plus = mp.besseli(1/4, arg)    # I_{1/4}(ab/4)
bessel_sum = I_minus + I_plus    # Sum of Bessel functions

# Compute Gamma(1/4)
gamma_val = mp.gamma(1/4)

# Compute prefactor: sqrt(2π) * a^{-1/2}
prefactor = mp.sqrt(2 * mp.pi) * mp.power(a, -0.5)

# Combine all components for final result
result = prefactor * gamma_val * bessel_sum

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))