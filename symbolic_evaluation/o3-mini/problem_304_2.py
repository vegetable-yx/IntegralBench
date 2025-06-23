import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define the parameters for the hypergeometric function
a = mp.mpf(-3)/2  # First parameter: -3/2
b = mp.mpf(1)/2   # Second parameter: 1/2
c = 1             # Third parameter: 1
z = mp.mpf(1)/4   # Argument: 1/4

# Compute the hypergeometric function ₂F₁(-3/2, 1/2; 1; 1/4)
hyper_val = mp.hyp2f1(a, b, c, z)

# Multiply the result by π/6
result = (mp.pi / 6) * hyper_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))