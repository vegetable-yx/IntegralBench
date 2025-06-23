import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a'. Here we choose a=1 for computation.
a = mp.mpf(1)

# Compute the argument for the hypergeometric functions: -a^2/4
arg = -a**2 / 4

# Compute the constant factor: a * Gamma(3/4) / (2 * Gamma(5/4))
gamma_34 = mp.gamma(mp.mpf(3)/4)
gamma_54 = mp.gamma(mp.mpf(5)/4)
const_factor = (a * gamma_34) / (2 * gamma_54)

# Compute the first hypergeometric function: _1F_2(1/4; 3/2, 5/4; arg)
hyp1 = mp.hyper([mp.mpf(1)/4], [mp.mpf(3)/2, mp.mpf(5)/4], arg)

# First term: const_factor * hyp1
term1 = const_factor * hyp1

# Compute the second hypergeometric function: _1F_2(1/2; 5/4, 7/4; arg)
hyp2 = mp.hyper([mp.mpf(1)/2], [mp.mpf(5)/4, mp.mpf(7)/4], arg)

# Second term: (a^2 / 6) * hyp2
term2 = (a**2 / 6) * hyp2

# Final result: term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))