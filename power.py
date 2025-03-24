def power(a, b):
    result = 1
    while b > 0:
        result *= a
        b -= 1
    return result

# Örnek Kullanım
a = 2
b = 5
print(power(a, b))  # Çıktı: 32
