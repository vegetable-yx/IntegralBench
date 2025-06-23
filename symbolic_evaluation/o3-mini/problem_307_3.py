import mpmath as mp

# Set internal precision to 15 decimal places for calculations
mp.dps = 15

# Calculate the logarithmic part: π * ln((√2 + 1)/2)
sqrt2 = mp.sqrt(2)  # Compute square root of 2
log_arg = (sqrt2 + 1) / 2  # Argument for the logarithm: (√2 + 1)/2
log_part = mp.log(log_arg)  # Natural logarithm of the argument
pi_log = mp.pi * log_part  # Multiply by π

# Calculate the elliptic integral part: √2 * [2*E(1/√2) - K(1/√2)]
k_val = 1 / sqrt2  # Argument for the elliptic integrals: 1/√2
E_val = mp.ellipe(k_val)  # Complete elliptic integral of the second kind, E(k)
K_val = mp.ellipk(k_val)  # Complete elliptic integral of the first kind, K(k)
bracket = 2 * E_val - K_val  # Compute the expression inside the brackets
elliptic_part = sqrt2 * bracket  # Multiply by √2

# Sum the two main parts
result = pi_log + elliptic_part

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))