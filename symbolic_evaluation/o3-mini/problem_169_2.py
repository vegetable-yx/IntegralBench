import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Compute gamma(1/4)^2 and gamma(1/4)^4 for later use
gamma_14_sq = gamma_14**2
gamma_14_quad = gamma_14**4

# Calculate the first term: [sqrt(pi) * gamma(1/4)^2 / 12] times the hypergeometric function
# Parameters for _3F_2: a = [1/2, 1/2, 1/2], b = [3/4, 5/4], z = 1/4
hyp = mp.hyper([mp.mpf(1)/2, mp.mpf(1)/2, mp.mpf(1)/2], 
               [mp.mpf(3)/4, mp.mpf(5)/4], 
               mp.mpf(1)/4)
first_part = (mp.sqrt(mp.pi) * gamma_14_sq / 12) * hyp

# Calculate the second term: gamma(1/4)^4 / (96 * pi)
second_part = gamma_14_quad / (96 * mp.pi)

# Combine the terms: I = first_part - second_part
result = first_part - second_part

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))