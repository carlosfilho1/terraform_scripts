import subprocess
import os
import re

terraform_directory = "/home/carlos/script/terraform_scripts/azure/storage-account"

location_map = {
    "0": "eastus",
    "1": "westus",
    "2": "westeurope"
}

# Exibir opções de regiões
print("Selecione a região para o location:")
for key, value in location_map.items():
    print(f"{key}: {value}")

# Obter a escolha do usuário
selected_location = input("Digite o número da região desejada: ")
region = location_map[selected_location]

# Função para validar o nome do Storage Account
def validar_nome_sa(nome_sa):
    if re.match("^[a-z0-9]{3,24}$", nome_sa):
        return True
    else:
        return False

# Solicitar nome da SA
while True:
    SA = input("Digite o nome do Storage Account (somente letras minúsculas e números, entre 3 e 24 caracteres): ")
    if validar_nome_sa(SA):
        break
    else:
        print("Nome inválido. O nome deve conter apenas letras minúsculas e números, e deve ter entre 3 e 24 caracteres.")

os.chdir(terraform_directory)


location_map_sa = {
    "0": "BlobStorage",
    "1": "BlockBlobStorage",
    "2": "FileStorage",
    "3": "Storage",
    "4": "StorageV2"
    # Default do tipo account "StorageV2"
}
# Exibir o tipo account storage
print("Selecione a região para o location:")
for key, value in location_map_sa.items():
    print(f"{key}: {value}")

# Obter a escolha do usuário
selected_sa = input("Digite o tipo do storage account: ")
storage_account = location_map_sa[selected_sa]


# account_replication_type
location_map_replication = {
    "0": ""
}
print("Selecione a opção de redudância para serviço de armazenamento azure")





# Subescrever o arquivo.
with open('location-txt.tfvars', 'w') as f:
    f.write(f'user_selected_location = "{region}"\n')
    f.write(f'SA = "{SA}"\n')
    f.write(f'type_SA = "{storage_account}"\n')


# terraform plan
os.system("terraform plan -lock=false -var-file=location-txt.tfvars")

# Terraform Apply
execute_apply = input("Deseja executar o terraform apply? (s/n): ")

if execute_apply.lower() == 's':
    os.system("terraform apply -lock=false -var-file=location-txt.tfvars -auto-approve")
else:
    print("Execução do terraform apply cancelada.")



# import subprocess
# import os

# terraform_directory = "/home/carlos/script/terraform_scripts/azure/storage-account"

# location_map = {
#     "0": "eastus",
#     "1": "westus",
#     "2": "westeurope"
# }

# # Exibir opções de regiões
# print("Selecione a região para o location:")
# for key, value in location_map.items():
#     print(f"{key}: {value}")

# # Obter a escolha do usuário
# selected_location = input("Digite o número da região desejada: ")
# region = location_map[selected_location]

# # nome da SA
# SA = input("Digite o nome do Storage Account: ")


# os.chdir(terraform_directory)

# # Subescrever o arquivo.
# with open('location-txt.tfvars', 'w') as f:
#     f.write(f'user_selected_location = "{region}"\n')
#     f.write(f'SA = "{SA}"\n')

# # terraform plan
# os.system("terraform plan -lock=false -var-file=location-txt.tfvars")


# # Terraform Apply
# execute_apply = input("Deseja executar o terraform apply? (s/n): ")

# if execute_apply.lower() == 's':
#     os.system("terraform apply -lock=false -var-file=location-txt.tfvars -auto-approve")
# else:
#     print("Execução do terraform apply cancelada.")
