import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Define parameters a and b (user must set these values)
# Example: a = 1.0, b = 1.0
# Calculate square root of a
sqrt_a = mp.sqrt(a)

# Calculate the argument for the hypergeometric function: (b² * a)/4
arg = (b**2 * a) / 4

# Compute the confluent hypergeometric limit function ₀F₁(; 3/2; arg)
hyp_val = mp.hyp0f1(mp.mpf(3)/2, arg)

# Multiply components: 2 * sqrt(a) * hypergeometric value
result = 2 * sqrt_a * hyp_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))

**Important Note:** The user must define numerical values for `a` and `b` before running this code. The example values `a = 1.0` and `b = 1.0` are placeholders - replace them with your actual parameters.