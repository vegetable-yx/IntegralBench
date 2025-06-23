import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the first term: pi * ln((1 + sqrt(5))/2)
# Step 1: Calculate the golden ratio numerator (1 + sqrt(5))
numerator = 1 + mp.sqrt(5)
# Step 2: Divide by 2 to get the golden ratio constant
golden_ratio = numerator / 2
# Step 3: Take the natural logarithm
log_term = mp.log(golden_ratio)
# Step 4: Multiply by pi
term1 = mp.pi * log_term

# Compute the second term: (pi/2) * atan(1/2)
# Step 1: Calculate arctan of 0.5
atan_term = mp.atan(0.5)
# Step 2: Multiply by pi/2
term2 = (mp.pi / 2) * atan_term

# Combine the terms: term1 - term2
result = term1 - term2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))