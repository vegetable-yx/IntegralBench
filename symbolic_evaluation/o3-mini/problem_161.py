import mpmath as mp

# Set internal precision to 15 decimal places for accurate calculations
mp.dps = 15

# Example values for a and b (replace with actual values as needed)
a = 1.0
b = 1.0

# Step 1: Compute Γ(5/4) and Γ(3/4)
gamma_5_4 = mp.gamma(5/4)  # Gamma function at 5/4
gamma_3_4 = mp.gamma(3/4)  # Gamma function at 3/4

# Step 2: Compute the exponent term: exp(b^2 * a / 8)
exponent_arg = b**2 * a / 8  # Argument for exponential
exp_term = mp.exp(exponent_arg)  # Exponential function

# Step 3: Compute the argument for the Whittaker W function: z = b^2 * a / 4
z_val = b**2 * a / 4

# Step 4: Compute the Whittaker W function: W_{-1/4, -1/2}(z_val)
whittaker_term = mp.whitw(-1/4, -1/2, z_val)  # Whittaker W function

# Step 5: Multiply all components together: a * Γ(5/4) * Γ(3/4) * exp_term * whittaker_term
result = a * gamma_5_4 * gamma_3_4 * exp_term * whittaker_term

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))