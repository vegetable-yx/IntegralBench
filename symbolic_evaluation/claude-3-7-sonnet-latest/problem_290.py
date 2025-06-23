import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Define the value of 'a' (user can change this value as needed)
a = 1.0  # Example value; replace with desired input

# Calculate the first term: π/(4a²)
term1 = mp.pi / (4 * a**2)

# Calculate the exponential factor: e^{-a}
exp_factor = mp.exp(-a)

# Calculate the modified Bessel function of the first kind: I₁(a)
bessel_term = mp.besseli(1, a)

# Calculate the second term: (π/(2a²)) * e^{-a} * I₁(a)
term2 = (mp.pi / (2 * a**2)) * exp_factor * bessel_term

# Combine terms: term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))