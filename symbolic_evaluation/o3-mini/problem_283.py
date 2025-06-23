import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sqrt(5) once for reuse
sqrt5 = mp.sqrt(5)

# First term: (π/4) * ln((sqrt(5) + 1)/2)
numerator1 = sqrt5 + 1
fraction1 = numerator1 / 2
log_term = mp.log(fraction1)
term1 = (mp.pi / 4) * log_term

# Second term: (sqrt(5)/2) * arctan(2/sqrt(5))
arg2 = 2 / sqrt5
atan_val2 = mp.atan(arg2)
term2 = (sqrt5 / 2) * atan_val2

# Third term: -1/2 * arctan(2)
atan_val3 = mp.atan(2)
term3 = -0.5 * atan_val3

# Sum all terms
result = term1 + term2 + term3

# Print result rounded to 10 decimal places
print(mp.nstr(result, n=10))