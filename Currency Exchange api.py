import requests

base = input("Enter your Currency type : ")
target = input("Enter the type of target currency : ")
url = f"https://v6.exchangerate-api.com/v6/5dc5dfdca44c636aa47a0ce7/pair/{base}/{target}"

response = requests.get(url)
data = response.json()
amount = int(input("Enter the amount u want to convert : "))

print(f"{amount} {base} = {amount * data['conversion_rate']:.2f} {target}")


