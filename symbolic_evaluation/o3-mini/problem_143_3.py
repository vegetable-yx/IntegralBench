import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the value of parameter 'a' (example value, can be changed by user)
a = 1.0

# Convert a to mpmath floating point number for high precision
a_mp = mp.mpf(a)

# Compute z = a^2 / 4
z = (a_mp ** 2) / 4

# Parameters for the hypergeometric function {}_{1}F_{2}
# Numerator parameters: [1]
# Denominator parameters: [3/2, 2]
numerator_params = [1]
denominator_params = [mp.mpf('3/2'), 2]  # Using exact fraction for 3/2

# Evaluate the hypergeometric function
hyper_val = mp.hyper(numerator_params, denominator_params, z)

# Multiply by π/8
pi = mp.pi
result = (pi / 8) * hyper_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))