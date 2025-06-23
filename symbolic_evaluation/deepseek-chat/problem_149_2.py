import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute π^(3/2)
pi_power = mp.power(mp.pi, 1.5)

# Step 2: Compute the square root of 2
sqrt_two = mp.sqrt(2)

# Step 3: Compute Gamma(3/4)
gamma_3_4 = mp.gamma(0.75)

# Step 4: Square Gamma(3/4)
gamma_squared = gamma_3_4 ** 2

# Step 5: Compute the denominator: sqrt(2) * [Gamma(3/4)]^2
denominator = sqrt_two * gamma_squared

# Step 6: Compute the final result: π^(3/2) / denominator
result = pi_power / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))