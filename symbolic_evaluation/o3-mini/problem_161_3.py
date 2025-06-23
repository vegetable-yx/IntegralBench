import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Define input parameters (user must set these before running)
a = mp.mpf(1)  # Example value for a, replace with desired value
b = mp.mpf(1)  # Example value for b, replace with desired value

# Compute the argument for Bessel and exponential functions
z = (b * mp.sqrt(a)) / 2

# Compute the exponential factor: exp(z)
exp_factor = mp.exp(z)

# Compute the two modified Bessel functions of the first kind
I_minus = mp.besseli(-0.25, z)  # I_{-1/4}(z)
I_plus = mp.besseli(0.25, z)    # I_{1/4}(z)

# Sum the Bessel functions
bessel_sum = I_minus + I_plus

# Compute the constant factor: π * a^{3/4} / 2
a_power = a ** (mp.mpf(3)/4)  # a^{3/4}
const_factor = (mp.pi * a_power) / 2

# Combine all components to get final result
result = const_factor * exp_factor * bessel_sum

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))