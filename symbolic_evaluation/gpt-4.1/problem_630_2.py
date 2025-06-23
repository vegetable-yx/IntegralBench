import mpmath as mp

# Set internal decimal places to 15 for high precision
mp.dps = 15

# Compute the first term: \frac{\pi \ln 3}{12\sqrt{3}}
numerator = mp.pi * mp.log(3)  # pi * ln(3)
denominator = 12 * mp.sqrt(3)  # 12 * sqrt(3)
term1 = numerator / denominator

# The integral \int_{\pi/6}^{\pi/3} \ln(\tan\theta) d\theta is known to be zero
integral_value = 0

# Compute the second term: \frac{1}{\sqrt{3}} times the integral
factor = 1 / mp.sqrt(3)
term2 = factor * integral_value

# Combine both terms
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))