import requests
import subprocess

# Define a URL do site que você deseja testar
url = "http://0.0.0.0:8080/"

# Define o endereço IP do proxy e a porta
proxy = {
  "http": f"{}",
  "https": f"{}"
}

# Define os parâmetros do SQLmap
sqlmap_options = "-u {} --batch --random-agent --proxy {} --dump".format(url, proxy["http"])

# Executa o SQLmap com os parâmetros definidos
output = subprocess.check_output(["sqlmap", sqlmap_options])

# Exibe a saída do SQLmap
print(output)