import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters a and b - replace values as needed
a = mp.mpf('1.0')
b = mp.mpf('1.0')

# Calculate the argument for the Bessel function: (a*b)/2
arg = (a * b) / 2

# Compute the modified Bessel function of the first kind of order 1/4
bessel_term = mp.besseli(0.25, arg)  # I_{1/4}(ab/2)

# Calculate constant: sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)

# Calculate constant: 2^{1/4}
two_power = mp.power(2, 0.25)

# Calculate a^{1/4}
a_power = mp.power(a, 0.25)

# Calculate b^{1/4}
b_power = mp.power(b, 0.25)

# Combine terms: numerator = sqrt(pi) * 2^{1/4} * a^{1/4}
numerator = sqrt_pi * two_power * a_power

# Compute the entire expression: (numerator / b^{1/4}) * I_{1/4}(ab/2)
result = (numerator / b_power) * bessel_term

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))