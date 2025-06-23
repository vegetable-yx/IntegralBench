import mpmath as mp
mp.dps = 15

a = mp.mpf(1)/4
series_sum = mp.mpf(0)
k = 1
tolerance = mp.mpf(1e-15)

while True:
    a_power = a**(2*k)
    k_sq = k**2
    fact_k = mp.factorial(k)
    denominator = k_sq * fact_k**2
    term = a_power / denominator
    series_sum += term
    if abs(term) < tolerance:
        break
    k += 1

result = (mp.pi/4) * series_sum
print(mp.nstr(result, n=10))