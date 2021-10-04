string = input('Insira aqui a palavra: ')

def print_substring(substring, initial_index, final_index):
    if final_index < len(substring):
        print(f"{substring[initial_index : final_index + 1]}, ", end="")
        print_substring(substring, initial_index, final_index + 1)
    else:
        print()
    
for i in range(len(string)):
    print_substring(string, i, i)