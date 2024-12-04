import os
import subprocess

def list_directory(path):
    """List all files and directories in the given path."""
    try:
        items = os.listdir(path)
        print(f"\nDirectory: {path}\n")
        print("0. .. (Go back)")  # Option to go back to the parent directory
        for idx, item in enumerate(items, 1):
            print(f"{idx}. {item}")
        return items
    except FileNotFoundError:
        print("Directory not found.")
        return []

def choose_program_to_run(path, items):
    """Ask the user to choose a program or directory."""
    choice = input("\nEscolha um número, navegue nos diretórios, '0' para voltar ou 'q' para sair: ")
    
    if choice.lower() == 'q':
        return None
    
    try:
        choice_idx = int(choice)
        if choice_idx == 0:
            return '..'  # Special option to go back to the parent directory
        
        selected_item = items[choice_idx - 1]  # Subtract 1 because option 0 is "go back"
        full_path = os.path.join(path, selected_item)
        
        if os.path.isdir(full_path):
            return full_path  # If it's a directory, return the directory path
        elif os.path.isfile(full_path) and full_path.endswith(".py"):
            return full_path  # If it's a Python file, return the file path
        else:
            print("Invalid choice or not a Python file.")
            return None
    except (ValueError, IndexError):
        print("Invalid input.")
        return None

def run_python_program(program_path):
    """Run the chosen Python program using subprocess."""
    if program_path and program_path.endswith(".py"):
        print(f"\nRodando programa: {program_path}")
        subprocess.run(["python", program_path])
    else:
        print("Arquivo inválido.")

def main():
    current_directory = os.getcwd()  # Start from the current directory
    while True:
        items = list_directory(current_directory)
        selected = choose_program_to_run(current_directory, items)
        
        if selected is None:
            print("Saindo...")
            break
        elif selected == '..':
            current_directory = os.path.dirname(current_directory)  # Move to parent directory
        elif os.path.isdir(selected):
            current_directory = selected  # Navigate into the directory
        else:
            run_python_program(selected)
            input("\nPressione Enter para retornar ao menu...")  # Pause before returning to menu

if __name__ == "__main__":
    main()
