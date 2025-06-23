import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant factor: 2^{3/4} * Gamma(3/4) / (2 * sqrt(pi))
factor = mp.power(2, 3/4) * mp.gamma(3/4) / (2 * mp.sqrt(mp.pi))

# Compute the argument for the Bessel functions: sqrt(2)
arg = mp.sqrt(2)

# Compute the two Bessel functions: J_{-1/4}(sqrt(2)) and J_{3/4}(sqrt(2))
J_neg_quarter = mp.besselj(-1/4, arg)
J_three_quarter = mp.besselj(3/4, arg)

# Compute the expression inside the brackets: sqrt(2)*J_{-1/4}(sqrt(2)) - J_{3/4}(sqrt(2))
bracket_term = mp.sqrt(2) * J_neg_quarter - J_three_quarter

# Multiply the constant factor by the bracket term
result = factor * bracket_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))