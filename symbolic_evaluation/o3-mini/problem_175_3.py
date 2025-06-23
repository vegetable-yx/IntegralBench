import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute gamma functions
gamma_3_4 = mp.gamma(mp.mpf(3)/4)  # Gamma(3/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)  # Gamma(5/4)

# Compute constant factor: [π * (Gamma(3/4))^2] / [16 * (Gamma(5/4))^2]
numerator_const = mp.pi * (gamma_3_4 ** 2)
denominator_const = 16 * (gamma_5_4 ** 2)
constant_factor = numerator_const / denominator_const

# Compute the hypergeometric function {}_3F_2(1/2,1/2,1/2; 3/4,5/4; 1/4)
hyper_term = mp.hyper3f2(mp.mpf(1)/2, mp.mpf(1)/2, mp.mpf(1)/2,  # a1, a2, a3
                         mp.mpf(3)/4, mp.mpf(5)/4,              # b1, b2
                         mp.mpf(1)/4)                           # z

# Compute the expression inside the braces: hypergeometric result minus 2
inner_expression = hyper_term - 2

# Multiply constant factor by inner expression
result = constant_factor * inner_expression

# Print final result to 10 decimal places
print(mp.nstr(result, n=10))