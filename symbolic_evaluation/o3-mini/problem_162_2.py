import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (replace with actual values as needed)
a = 1.0
b = 1.0

# Precompute common subexpression: b^2 * a
b2a = b**2 * a

# Calculate argument for Whittaker function and exponential
whitaker_arg = b2a / 16.0
exponential_arg = b2a / 32.0

# Compute exponential factor: exp(b^2*a/32)
exp_factor = mp.exp(exponential_arg)

# Compute Whittaker function: W_{-1/4,0}(b^2*a/16)
whit_val = mp.whitw(-0.25, 0, whitaker_arg)

# Compute Gamma(3/4)
gamma_val = mp.gamma(0.75)

# Compute power factors: 2^(3/4) and a^(1/2)
two_power = mp.power(2, 0.75)
a_sqrt = mp.sqrt(a)

# Combine all factors into final result
result = two_power * a_sqrt * gamma_val * exp_factor * whit_val

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))