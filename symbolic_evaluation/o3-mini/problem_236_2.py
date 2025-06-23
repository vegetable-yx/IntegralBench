import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the constant factor: pi * sqrt(2) / 4
constant_factor = mp.pi * mp.sqrt(2) / 4

# Compute the hypergeometric function 2F1(1, 3/2; 2; 1/4)
hypergeometric_value = mp.hyp2f1(1, mp.mpf(3)/2, 2, mp.mpf(1)/4)

# Multiply the constant factor by the hypergeometric function
result = constant_factor * hypergeometric_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))