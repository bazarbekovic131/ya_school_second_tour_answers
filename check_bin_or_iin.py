from dadata import Dadata
token = "Some Token Placeholder"
dadata = Dadata(token)
query = input("Enter BIN")
query = query.strip()

result = dadata.find_by_id("party_kz", query)
print(result)
