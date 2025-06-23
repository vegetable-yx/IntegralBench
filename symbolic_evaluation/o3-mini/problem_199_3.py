import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Define the argument for the Bessel functions
arg = 1 / mp.sqrt(2)

# Compute Bessel J functions for orders -1/4 and 1/4
j_neg_quarter = mp.besselj(-0.25, arg)
j_pos_quarter = mp.besselj(0.25, arg)

# Compute the difference: J_{-1/4}(arg) - J_{1/4}(arg)
bessel_diff = j_neg_quarter - j_pos_quarter

# Compute the constant factors: 2^{1/4} and sqrt(pi)
factor1 = mp.power(2, 0.25)  # 2^(1/4)
factor2 = mp.sqrt(mp.pi)      # sqrt(pi)

# Multiply the factors by the Bessel difference
result = factor1 * factor2 * bessel_diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))