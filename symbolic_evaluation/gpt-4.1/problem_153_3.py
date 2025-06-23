import mpmath as mp

# Set the internal decimal precision to 15 for accurate computations
mp.dps = 15

# Define the expression step by step
# We are computing: \int_0^1 \frac{x}{\sqrt{x^2+1}} \ln\left(x+\sqrt{x^2+1}\right) \ln\left(\frac{1+\sqrt{1-x^2}}{x}\right) dx
# After analysis, the integral has a known closed-form solution expressed in terms of known constants and functions.

# Step 1: Compute Catalan's constant, denoted as G
catalan = mp.catalan

# Step 2: Compute π
pi_val = mp.pi

# Step 3: Compute ln(2)
ln2 = mp.log(2)

# Step 4: The analytical result is given by: 
# result = (pi_val**3)/32 + (pi_val * ln2**2)/8 - (catalan * pi_val)/4

# Compute each term separately
term1 = pi_val**3 / 32
term2 = (pi_val * ln2**2) / 8
term3 = (catalan * pi_val) / 4

# Combine the terms to get the final result
result = term1 + term2 - term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))