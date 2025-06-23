import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute gamma(1/4)
gamma_14 = mp.gamma(0.25)

# Raise gamma(1/4) to the 4th power
gamma_14_4 = gamma_14**4

# Compute denominator: 32 * sqrt(2 * pi)
denominator = 32 * mp.sqrt(2 * mp.pi)

# Compute the hypergeometric function: _2F_1(1/4, 1/2; 3/4; 1/4)
hypergeom = mp.hyp2f1(0.25, 0.5, 0.75, 0.25)

# Combine the components: (gamma_14_4 / denominator) * hypergeom
result = (gamma_14_4 / denominator) * hypergeom

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))