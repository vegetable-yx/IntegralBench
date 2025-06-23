import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define input parameters (modify these as needed)
a = 1.0
b = 1.0

# Compute sqrt(πa) component
sqrt_pi_a = mp.sqrt(mp.pi * a)

# Calculate the argument for the hypergeometric function: (b²a)/4
hyper_arg = (b**2 * a) / 4

# Compute the hypergeometric function ₀F₁(; 3/2; hyper_arg)
hyper_result = mp.hyp0f1(1.5, hyper_arg)

# Combine components for final result
result = sqrt_pi_a * hyper_result

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))