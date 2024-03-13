def is_palindrome_recursive(word, low_index, high_index):
    # Caso base: string vazia é palíndromo
    if low_index >= high_index:
        return True

    # Verifica se os caracteres correspondentes são iguais
    if word[low_index] == word[high_index]:
        # Chama recursivamente com os índices ajustados
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False


# Função auxiliar para facilitar a chamada da função principal
def is_palindrome(word):
    return is_palindrome_recursive(word, 0, len(word) - 1)
