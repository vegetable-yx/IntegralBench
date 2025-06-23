import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi
pi_val = mp.pi

# Compute the first term: -(π^3 / 8) * log(2)
# Step 1: Compute π^3
pi_cubed = pi_val ** 3
# Step 2: Divide by 8
pi_cubed_over_8 = pi_cubed / 8
# Step 3: Compute log(2)
log2 = mp.log(2)
# Step 4: Multiply and negate
term1 = -pi_cubed_over_8 * log2

# Compute the second term: π * ζ(3)
# Step 1: Compute ζ(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)
# Step 2: Multiply by π
term2 = pi_val * zeta3

# Sum the two terms
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))