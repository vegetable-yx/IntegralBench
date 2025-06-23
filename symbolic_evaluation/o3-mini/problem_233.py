import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Define the parameters for the hypergeometric function
a = mp.mpf(3)/2  # First parameter
b = mp.mpf(1)/4  # Second parameter
c = mp.mpf(1)    # Third parameter
z = mp.mpf(1)/4  # Argument

# Compute the hypergeometric function ₂F₁(a, b; c; z)
hyp_val = mp.hyp2f1(a, b, c, z)

# Compute π * √2
pi_sqrt2 = mp.pi * mp.sqrt(2)

# Multiply to get the final result
result = pi_sqrt2 * hyp_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))