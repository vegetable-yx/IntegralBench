import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Step 1: Compute the intermediate value (√5 - 1)/2
sqrt5 = mp.sqrt(5)  # Calculate square root of 5
numerator = sqrt5 - 1  # √5 - 1
fraction = numerator / 2  # (√5 - 1)/2

# Step 2: Compute the logarithmic term: (1/2) * ln((√5 - 1)/2)
log_term = mp.log(fraction)  # Natural logarithm of the fraction
log_part = 0.5 * log_term  # Multiply by 1/2

# Step 3: Combine all terms: 1 - fraction - log_part
result = 1 - fraction - log_part

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))