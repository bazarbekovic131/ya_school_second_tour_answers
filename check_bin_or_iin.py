from dadata import Dadata
token = "e304ac4afb35e2cf2e700c07de32fda8e92a34e6"
dadata = Dadata(token)
query = input("Enter BIN")
query = query.strip()

result = dadata.find_by_id("party_kz", query)
print(result)
