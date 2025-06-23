import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Step 1: Compute the square root of π
sqrt_pi = mp.sqrt(mp.pi)

# Step 2: Compute Gamma(1/4)
gamma_quarter = mp.gamma(mp.mpf('0.25'))

# Step 3: Square the Gamma(1/4) result
gamma_squared = gamma_quarter ** 2

# Step 4: Multiply sqrt(π) by the squared gamma value
numerator = sqrt_pi * gamma_squared

# Step 5: Compute the square root of 2
sqrt_2 = mp.sqrt(2)

# Step 6: Divide the numerator by sqrt(2) to get final result
result = numerator / sqrt_2

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))