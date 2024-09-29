import subprocess
import os

terraform_directory = "/home/carlos/script/terraform_scripts/azure/vm"

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

# nome da VM
vm_name = input("Digite o nome da máquina virtual: ")


os.chdir(terraform_directory)

# Subescrever o arquivo.
with open('location-txt.tfvars', 'w') as f:
    f.write(f'user_selected_location = "{region}"\n')
    f.write(f'vm_name = "{vm_name}"\n')

# terraform plan
os.system("terraform plan -lock=false -var-file=location-txt.tfvars")


# Terraform Apply
execute_apply = input("Deseja executar o terraform apply? (s/n): ")

if execute_apply.lower() == 's':
    os.system("terraform apply -lock=false -var-file=location-txt.tfvars -auto-approve")
else:
    print("Execução do terraform apply cancelada.")




# # prompt
# print("Selecione a região para o location:")
# for key, value in location_map.items():
#     print(f"{key}: {value}")

# selected_location = input("Digite o número da região desejada: ")


# # Validação
# if selected_location in location_map:
#     region = location_map[selected_location]
# else:
#     print("Região inválida. Usando a região padrão: eastus.")
#     region = "eastus"

# # Direcionar para o diretorio onde variavel está apontando
# os.chdir(terraform_directory)

# # Localização onde será subescrito o arquivo colocando a região.
# with open('terraform.tfvars', 'w') as f:
#     f.write(f'user_selected_location = "{region}"\n')

# # terraform plan
# try:
#     subprocess.run(["terraform", "plan", "-lock=false"], check=True)
# except subprocess.CalledProcessError as e:
#     print(f"Erro ao executar o terraform plan: {e}")