import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Calculate the denominator: 2^(5/4)
denom = 2**(mp.mpf(5)/4)

# Compute the first factor: pi / 2^(5/4)
factor1 = pi_val / denom

# Calculate the exponential factor: e^(-i*pi/8)
# Note: '1j' represents the imaginary unit in Python
exponent = -1j * pi_val / 8
factor2 = mp.exp(exponent)

# Compute the arctangent of (1 - i)
z = 1 - 1j
atan_val = mp.atan(z)

# Multiply all factors together
result = factor1 * factor2 * atan_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))