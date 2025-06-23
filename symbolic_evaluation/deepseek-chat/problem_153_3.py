import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the integral expression using known closed-form solution
# The integral is known to evaluate to π(π - 2ln2)/16

# Step 1: Compute π
pi_val = mp.pi

# Step 2: Compute ln(2)
ln2 = mp.log(2)

# Step 3: Compute the expression inside: π - 2ln2
inner = pi_val - 2 * ln2

# Step 4: Multiply by π: π(π - 2ln2)
product = pi_val * inner

# Step 5: Divide by 16 to get final result
result = product / 16

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))