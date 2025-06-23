import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the constant factor: π * √2
constant_factor = mp.pi * mp.sqrt(2)

# Parameters for the hypergeometric function ₂F₁
a = mp.mpf(3)/2  # First parameter: 3/2
b = mp.mpf(1)/2  # Second parameter: 1/2
c = 1            # Third parameter: 1
z = mp.mpf(1)/4  # Argument: 1/4

# Compute the hypergeometric function ₂F₁(a, b; c; z)
hyper_val = mp.hyp2f1(a, b, c, z)

# Multiply constant factor by the hypergeometric function result
result = constant_factor * hyper_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))