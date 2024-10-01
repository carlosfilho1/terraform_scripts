import subprocess
import os

# Função para ler credenciais de um arquivo txt
def read_credentials(file_path):
    credentials = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Ignora linhas vazias ou que não contenham "="
            if "=" in line:
                key, value = line.strip().split(' = ', 1)  # Split na primeira ocorrência de "="
                credentials[key.strip()] = value.strip()   # Remove espaços em branco em torno de chave/valor
    return credentials

# Função para gerar o arquivo terraform.tfvars
def generate_tfvars(credentials, output_file='terraform.tfvars'):
    required_keys = ['subscription_id', 'client_id', 'client_secret', 'tenant_id']

    # Verifica se todas as chaves necessárias estão presentes
    for key in required_keys:
        if key not in credentials:
            raise KeyError(f"A chave '{key}' não foi encontrada nas credenciais!")

    with open(output_file, 'w') as file:
        file.write(f'subscription_id = "{credentials["subscription_id"]}"\n')
        file.write(f'client_id       = "{credentials["client_id"]}"\n')
        file.write(f'client_secret   = "{credentials["client_secret"]}"\n')
        file.write(f'tenant_id       = "{credentials["tenant_id"]}"\n')

# Caminho do arquivo de credenciais
file_path = '../credentials.txt'

# Lendo o arquivo e gerando terraform.tfvars
credentials = read_credentials(file_path)
generate_tfvars(credentials)

print("Arquivo terraform.tfvars gerado com sucesso!")

def delete_tfvars(file_path='terraform.tfvars'):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Arquivo {file_path} excluído com sucesso.")
    else:
        print(f"O arquivo {file_path} não existe.")





terraform_directory = "/home/carlos/script/terraform_scripts/azure/storage-account"
tfvars_file = "location-txt.tfvars"


def get_variable_from_tfvars(variable_name, tfvars_file):
    with open(tfvars_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(variable_name):
                return line.split('=')[1].strip().replace('"', '')
    return None

# diretório do Terraform
os.chdir(terraform_directory)

region = get_variable_from_tfvars("user_selected_location", tfvars_file)
SA = get_variable_from_tfvars("SA", tfvars_file)


if region and SA:
    print(f"VM Name: {SA}")
    print(f"Região selecionada: {region}")


    os.system(f"terraform plan -destroy -lock=false -var-file={tfvars_file}")

    # terraform destroy
    execute_destroy = input(f"Deseja destruir o Storange Account '{SA}' localizada em '{region}'? (s/n): ")

    if execute_destroy.lower() == 's':
        # terraform destroy execução
        os.system(f"terraform destroy -lock=false -var-file={tfvars_file} -auto-approve")
        delete_tfvars()
    else:
        print("Execução do terraform destroy cancelada.")
        delete_tfvars()
else:
    print(f"Erro ao obter dados de localização ou nome da VM do arquivo {tfvars_file}.")
