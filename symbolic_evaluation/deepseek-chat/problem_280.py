import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define input parameters (example values, can be modified by user)
a = mp.mpf('1.0')
b = mp.mpf('1.0')

# Calculate the argument for the Bessel functions
arg = (b * a) / 4

# Compute the modified Bessel functions of the first kind
I_plus = mp.besseli(0.25, arg)  # I_{1/4}(b a / 4)
I_minus = mp.besseli(-0.25, arg)  # I_{-1/4}(b a / 4)

# Compute pi^(3/2)
pi_power = mp.pi ** (mp.mpf(3)/2)

# Compute a^(1/2)
a_sqrt = mp.sqrt(a)

# Combine multiplicative factors: (pi^{3/2} * a^{1/2}) / 2
factor = (pi_power * a_sqrt) / 2

# Multiply by the Bessel functions to get final result
result = factor * I_plus * I_minus

# Print result to 10 decimal places
print(mp.nstr(result, n=10))