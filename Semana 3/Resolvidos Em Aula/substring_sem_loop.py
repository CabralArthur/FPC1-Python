string = input('Insira aqui a palavra: ')

def print_substring(substring, initial_index, final_index):
    if(initial_index) < len(substring):
        if final_index < len(substring):
            print(f"{substring[initial_index : final_index + 1]}, ", end="")
            print_substring(substring, initial_index, final_index + 1)
        else:
            print()
            print_substring(substring, initial_index + 1, initial_index + 1)

print_substring(string, 0, 0)