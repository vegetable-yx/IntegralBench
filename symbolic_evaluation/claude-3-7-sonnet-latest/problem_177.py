import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (user can modify this value as needed)
a = 1.0  # Example value; replace with desired input

# Calculate components of the expression
# First term: (π/a) * Si(a) * sin(a)
si_a = mp.si(a)       # Sine integral of a
sin_a = mp.sin(a)     # Sine of a
term1 = (mp.pi / a) * si_a * sin_a

# Components inside the second term: ln(a) + γ + Ci(2a)
ln_a = mp.log(a)      # Natural logarithm of a
gamma = mp.euler      # Euler-Mascheroni constant
ci_2a = mp.ci(2*a)    # Cosine integral of 2a
inner_sum = ln_a + gamma + ci_2a

# Second term: (π/(2a)) * [ln(a) + γ + Ci(2a)]
term2 = (mp.pi / (2 * a)) * inner_sum

# Combine terms: result = term1 - term2
result = term1 - term2

# Print final result with 10 decimal places
print(mp.nstr(result, n=10))