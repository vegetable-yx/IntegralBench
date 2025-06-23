import mpmath as mp

# Set the internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute Γ(1/4) and raise it to the 8th power
gamma_quarter = mp.gamma(mp.mpf(1)/4)
gamma_quarter_power8 = gamma_quarter**8

# Compute the denominator: 2^15 * π^2
denominator = (2**15) * (mp.pi**2)

# Calculate the first part: Γ(1/4)^8 / (2^15 * π^2)
part1 = gamma_quarter_power8 / denominator

# Define parameters for the generalized hypergeometric function 4F3
# Numerators: [1/4, 1/4, 3/4, 3/4]
a_params = [mp.mpf(1)/4, mp.mpf(1)/4, mp.mpf(3)/4, mp.mpf(3)/4]
# Denominators: [1, 3/2, 3/2]
b_params = [1, mp.mpf(3)/2, mp.mpf(3)/2]
# Argument: 1/16
z_val = mp.mpf(1)/16

# Compute the hypergeometric function part
hyper_part = mp.hyper(a_params, b_params, z_val)

# Multiply both parts to get the final result
result = part1 * hyper_part

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))