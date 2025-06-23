import mpmath as mp

# Set internal decimal places for high precision calculations
mp.dps = 15

# Define the value of 'a' (example value; can be adjusted)
a = mp.mpf(1.0)

# Calculate common constants and parameters
pi = mp.pi
a_squared = a * a
z = a_squared / 4  # Argument for hypergeometric functions

# Define fractional parameters as mpmath floats for precision
one_quarter = mp.mpf(1)/4
three_quarter = mp.mpf(3)/4
one_half = mp.mpf(1)/2
three_half = mp.mpf(3)/2
five_quarter = mp.mpf(5)/4

# Compute Gamma function values
gamma_14 = mp.gamma(one_quarter)
gamma_34 = mp.gamma(three_quarter)
gamma_54 = mp.gamma(five_quarter)

# Compute the first term: [sqrt(pi)*Gamma(1/4)/(4*Gamma(3/4))] * _1F_2(1/4; 1/2, 3/4; z)
coeff1 = (mp.sqrt(pi) * gamma_14) / (4 * gamma_34)
hyper1 = mp.hyper([one_quarter], [one_half, three_quarter], z)
term1 = coeff1 * hyper1

# Compute the second term: [a*sqrt(pi)*Gamma(3/4)/(8*Gamma(5/4))] * _1F_2(3/4; 3/2, 5/4; z)
coeff2 = (a * mp.sqrt(pi) * gamma_34) / (8 * gamma_54)
hyper2 = mp.hyper([three_quarter], [three_half, five_quarter], z)
term2 = coeff2 * hyper2

# Sum the terms to get the final result
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))