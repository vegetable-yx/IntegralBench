import mpmath as mp

# Set internal precision
mp.dps = 15

# Calculate intermediate values
# Step 1: Compute the sine of pi/3
sin_pi_3 = mp.sin(mp.pi/3)

# Step 2: Compute the cosine of pi/4
cos_pi_4 = mp.cos(mp.pi/4)

# Step 3: Compute the natural logarithm of 2
ln_2 = mp.log(2)

# Step 4: Compute the exponential of -1
exp_minus1 = mp.exp(-1)

# Step 5: Combine intermediate results
numerator = sin_pi_3 * cos_pi_4
denominator = ln_2 * exp_minus1
result = numerator / denominator

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))