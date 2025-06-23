import mpmath as mp

# Set internal decimal precision to 15 to ensure 10 decimal places accuracy
mp.dps = 15

# Compute the constant factor: (π * √2) / 4
pi_sqrt2 = mp.pi * mp.sqrt(2)
constant = pi_sqrt2 / 4

# Compute the hypergeometric function ₂F₁(3/2, 3/4; 2; 1/4)
hyp_val = mp.hyp2f1(mp.mpf('1.5'), mp.mpf('0.75'), 2, mp.mpf('0.25'))

# Multiply the constant factor by the hypergeometric function result
result = constant * hyp_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))