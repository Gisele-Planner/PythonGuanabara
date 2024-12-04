import os

#Utilitário para criar arquivos dos exercicios #fonte: chatgpt

# Definir o caminho da pasta onde os arquivos serão criados
folder_path = r"C:\Users\emers\OneDrive\Área de Trabalho\Exercicios Guanabara\Python3"

# Verificar se a pasta existe, se não, criar a pasta
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Criar arquivos do exe072.py até o exe114.py
for i in range(72, 115):
    file_name = f'exe{i:03}.py'  # Nome do arquivo no formato exe072.py, exe073.py, etc.
    file_path = os.path.join(folder_path, file_name)
    
    # Criar o arquivo vazio
    with open(file_path, 'w') as f:
        f.write(f"#exercicio {i:03} - Tema XYZ\n")
        f.write('''
print(('==*==')*20)
print('Bem vindo(a) - Tema XYZ')
print(('==*==')*20)'''
                )

print("Arquivos criados com sucesso!")
