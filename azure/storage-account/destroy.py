import subprocess
import os

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
    else:
        print("Execução do terraform destroy cancelada.")
else:
    print(f"Erro ao obter dados de localização ou nome da VM do arquivo {tfvars_file}.")
