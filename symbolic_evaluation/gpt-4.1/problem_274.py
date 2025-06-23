import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Example values for parameters a and b (user can modify these)
a = mp.mpf(1)
b = mp.mpf(1)

# Calculate argument for sinh and Bessel functions
arg = (b * a) / 2

# Compute hyperbolic sine term: 3 * sinh(ba/2)
term_sinh = 3 * mp.sinh(arg)

# Compute modified Bessel function term: π * I₂(ba/2)
# Note: I₂ denotes modified Bessel function of first kind, order 2
term_bessel = mp.pi * mp.besseli(2, arg)

# Sum the two terms inside the brackets
inner_sum = term_sinh + term_bessel

# Multiply by a²/(4b) to get final result
result = (a**2) / (4 * b) * inner_sum

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))