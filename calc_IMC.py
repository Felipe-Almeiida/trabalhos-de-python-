peso = float(input("digite o peso: "))
altura = float(input("digite a altura: "))

IMC = peso / altura ** 2
print(IMC)

if IMC < 17:
    print(f'muito abaixo do peso')
elif IMC < 18.5:
    print("abaixo do peso")
elif IMC < 24.99:
    print("peso normal")
elif IMC < 29.99:
    print("acima do peso")
elif IMC < 34.99:
    print("obesidade 1")
elif IMC < 39.99:
    print("obesidade 2")
else:
    print("obesidade 3")
