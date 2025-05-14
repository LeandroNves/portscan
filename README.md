# Port Scanner - by Leandro

![banner](https://img.shields.io/badge/Port%20Scanner-v1.0-blue)

Esta ferramenta é um scanner de portas multithreaded, desenvolvida por Leandro, projetada para verificar portas abertas em um host remoto. Ele pode ser configurado para escanear um intervalo de portas especificado ou uma lista de portas específicas.

## Características

- Escaneamento de portas utilizando múltiplas threads para aumentar a performance.
- Suporte para escanear portas específicas ou intervalos de portas.
- Exibição das portas abertas diretamente no console.
- Opção de salvar os resultados em um arquivo de saída.

## Requisitos

- Python 3.x
- Bibliotecas:
  - socket
  - argparse
  - threading
  - queue
  - datetime

## Como Usar

1. **Clonando o repositório:**

    ```bash
    git clone https://github.com/LeandroNves/portscan
    cd portscan
    ```

2. **Instalando Dependências:**

   Se necessário, instale as dependências utilizando:

    ```bash
    pip install -r requirements.txt
    ```

3. **Rodando o scanner:**

   Use o comando abaixo para rodar o scanner:

    ```bash
    python portscan.py [host] -p [portas] -o [arquivo_de_saida]
    ```

   - `[host]`: O endereço do host a ser escaneado (exemplo: google.com).
   - `-p [portas]`: A lista de portas a serem escaneadas, que pode ser passada como uma lista separada por vírgulas ou um intervalo de portas (exemplo: 22,80,1000-1010).
   - `-o [arquivo_de_saida]`: (Opcional) Caminho para um arquivo onde os resultados serão salvos.

### Exemplos:

- Escanear portas específicas no host `google.com`:

    ```bash
    python portscan.py google.com -p 22,80,443
    ```

- Escanear intervalo de portas no host `example.com`:

    ```bash
    python portscan.py example.com -p 1-1000
    ```

- Escanear portas específicas e salvar o resultado em um arquivo:

    ```bash
    python portscan.py example.com -p 80,443 -o result.txt
    ```

## Resultados

As portas abertas serão exibidas no console no formato:

```bash
[+] Port 80 open
[+] Port 443 open
