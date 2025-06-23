import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Example values for a and b (can be changed by user)
a = 1
b = 1

# Calculate the argument for the hypergeometric function
arg = (a**2 * b**2) / 16.0

# Compute the hypergeometric function 0F1(; 3/2; arg)
hyp_val = mp.hyp0f1(1.5, arg)  # 1.5 = 3/2

# Multiply by 2*sqrt(a)
result = 2 * mp.sqrt(a) * hyp_val

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))