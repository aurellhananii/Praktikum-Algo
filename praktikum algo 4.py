# Aurelia Clariza Hanani
# 065002500014

a = int(input("Masukkan sisi a: "))
b = int(input("Masukkan sisi b: "))
c = int(input("Masukkan sisi c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Segitiga sama sisi")
    elif a == b or a == c or b == c:
        print("Segitiga sama kaki")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Segitiga siku-siku")
    else:
        print("Segitiga sembarang")
else:
    print("Bukan segitiga")