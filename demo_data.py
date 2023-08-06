from cmkt.data import *
print("\nCMKT Data Subpackage Demo")
print()

# Load online resource files
print("Load url function")
result_json = load_url('https://world.openfoodfacts.org/api/v0/product/5060292302201.json')
print(result_json['code'])
print()

result_csv = load_url('https://gist.githubusercontent.com/rnirmal/e01acfdaf54a6f9b24e91ba4cae63518/raw/6b589a5c5a851711e20c5eb28f9d54742d1fe2dc/datasets.csv')
print(result_csv['about'][20])
print(len(result_csv['about']))
print()

# List CMKT dataset keys and all available cmkt datasets
print("List dataset keys and cmkt datasets function")
keys = ListDatasetKeys()
print(keys)
print()

# List CMKT datasets for the task of LID
print("List CMKT Datasets Function (search_key = task, search_term = ner): ")
data = ListDatasets(search_key="task", search_term = "ner", isPrint=True)
print()

# List CMKT datasets for hineng language
print("List CMKT Datasets Function (search_key = language, search_term = hineng): ")
data = ListDatasets(search_key="language", search_term = "hineng", isPrint=True)
print()

# Download cmkt datasets
print("Download cmkt datasets function")
lst = download_cmkt_datasets(["lid_hineng_Mave_ACL2018"])

print()
path = download_dataset_external('https://world.openfoodfacts.org/api/v0/product/5060292302201.json')

print()
print(lst)
print(path)