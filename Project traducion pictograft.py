dicionary = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k',
             'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u',
             'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a', ' ': ' ', '': '', 'A': 'B', 'B': 'C',
             'C': 'D', 'D': 'E', 'E': 'F', 'F': 'G', 'G': 'H', 'H': 'I', 'I': 'J', 'J': 'K', 'K': 'L', 'L': 'M',
             'M': 'N', 'N': 'O', 'O': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S', 'S': 'T', 'T': 'U', 'U': 'V', 'V': 'W',
             'W': 'X', 'X': 'Y', 'Y': 'Z', 'Z': 'A', '@': '?', '$': '!', '!': '@', '"': '#', ';': 'é', '<': 'ê',
             '^': 'á', '[': 'à', ']': 'â', '/': 'ã', '{': 'ó', '}': 'ô', '+': 'õ', '-': 'í', '§': 'ú', '=': 'û',
             '1': 'É', '2': 'Ê', '3': 'Á', '4': 'À', '5': 'Â', '6': 'Ã', '7': 'Ó', '8': 'Ô', '9': 'Õ', '0': 'Í',
             '(': 'Í', ')': 'Ú', '*': 'Û', '.': ',', ',': '.', '%': 'ç', '&': '-', '¹': '/', '£': '(', '¢': ')',
             'ª': '\n', '|': '"', '°': ':', '∞': '*', 'π': '0', '™': '1', '®': '2', '¥': '3', '©': '4', '±': '5',
             '≠': '6', '≤': '7', 'β': '8', 'α': '9'}

palavra = str(input('\nDigite a palavra que deseja descriptografar: '))
traduzido = ''.join(dicionary[letra] for letra in palavra)
print(traduzido)
