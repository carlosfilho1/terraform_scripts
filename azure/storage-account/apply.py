import subprocess
import os
import re

# Função para ler credenciais de um arquivo txt
def read_credentials(file_path):
    credentials = {}
    with open(file_path, 'r') as file:
        for line in file:
            if "=" in line:
                key, value = line.strip().split(' = ', 1)
                credentials[key.strip()] = value.strip()
    return credentials

# Criando arquivo terraform.tfvars
def generate_tfvars(credentials, output_file='terraform.tfvars'):
    required_keys = ['subscription_id', 'client_id', 'client_secret', 'tenant_id']

    # Validação de chaves
    for key in required_keys:
        if key not in credentials:
            raise KeyError(f"A chave '{key}' não foi encontrada nas credenciais!")

    with open(output_file, 'w') as file:
        file.write(f'subscription_id = "{credentials["subscription_id"]}"\n')
        file.write(f'client_id       = "{credentials["client_id"]}"\n')
        file.write(f'client_secret   = "{credentials["client_secret"]}"\n')
        file.write(f'tenant_id       = "{credentials["tenant_id"]}"\n')

file_path = '../credentials.txt'

credentials = read_credentials(file_path)
generate_tfvars(credentials)

print("Arquivo terraform.tfvars gerado com sucesso!")

def delete_tfvars(file_path='terraform.tfvars'):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Arquivo {file_path} excluído com sucesso.")
    else:
        print(f"O arquivo {file_path} não existe.")

# ---------------------------------------------------------


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


# ---------------------------------------------------------

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


# ---------------------------------------------------------

# account_replication_type
location_map_replication_type = {
    "0": "LRS",
    "1": "GRS",
    "2": "RAGRS",
    "3": "ZRS",
    "4": "GZRS",
    "5": "RAGZRS"
}

print("""
| Serviço                                               | LRS | ZRS | GRS | RA-GRS | GZRS  | RA-GZRS |
|-------------------------------------------------------|-----|-----|-----|--------|-------|---------|
| Armazenamento de blobs (incluindo Data Lake Storage)  | ✅   | ✅   | ✅   | ✅| ✅    | ✅     |
| Armazenamento de filas                                | ✅   | ✅   | ✅   | ✅| ✅    | ✅     |
| Armazenamento de mesa                                 | ✅   | ✅   | ✅   | ✅| ✅    | ✅     |
| Discos gerenciados do Azure                           | ✅   |      |       |   | ✅³   |         |
| Azure Elastic SAN                                     | ✅   |      |       |   |        |        |
| Arquivos do Azure                                     | ✅¹² | ✅¹² | ✅¹² | ✅¹| ✅¹  |        |

Notas de rodapé:
- ¹: Disponível para Premium FileShares.
- ²: Apenas para redundância de zona em contas de nível de conta de armazenamento.
- ³: Disponível para discos Ultra e Standard SSD.
      Selecione a opção de redudância para serviço de armazenamento azure
""")

for key, value in location_map_replication_type.items():
    print(f"{key}: {value}")

# Obter a escolha do usuário com validação
selected_replication_type = input("Digite o tipo do storage account (0 a 5): ").strip()

if selected_replication_type in location_map_replication_type:
    replication_type = location_map_replication_type[selected_replication_type]
    print(f"Tipo de replicação selecionado: {replication_type}")
else:
    print("Erro: Tipo de replicação inválido. Por favor, insira um valor entre 0 e 5.")


# ---------------------------------------------------------


# Subescrever o arquivo.
with open('location-txt.tfvars', 'w') as f:
    f.write(f'user_selected_location = "{region}"\n')
    f.write(f'SA = "{SA}"\n')
    f.write(f'type_SA = "{storage_account}"\n')
    f.write(f'type_replication_type = "{replication_type}"\n')


# terraform plan
os.system("terraform plan -lock=false -var-file=location-txt.tfvars")

# Terraform Apply
execute_apply = input("Deseja executar o terraform apply? (s/n): ").strip().lower()

if execute_apply == 's':
    os.system("terraform apply -lock=false -var-file=location-txt.tfvars -auto-approve")
    delete_tfvars()
elif execute_apply == 'n':
    print("Execução do terraform apply cancelada.")
else:
    print("Entrada inválida. Execução do terraform apply cancelada.")

# ---------------------------------------------------------




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
