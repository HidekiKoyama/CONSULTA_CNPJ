class Dados:
    def __init__(self, dados) -> None:
        self.__dados = dados
        self.__letras_especiais_dict = {
            'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'ä': 'a',
            'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
            'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
            'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o', 'ö': 'o', 'ø': 'o',
            'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
            'ñ': 'n',
            'ç': 'c',
            'ß': 's',
            'æ': 'ae',
            'œ': 'oe',
            'ø': 'o'
        }
        self.__caracteres_especiais = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '<', '>', ',', '.', '?', '/', '~', '`', "'", '"']
        self.__letras_alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def removeCaracterEspecial(self) -> None:
        for ce in self.__caracteres_especiais:
            self.__dados = self.__dados.replace(ce, "")
        
    def removeLetraEspecial(self)  -> None:
        for especial, letra in self.__letras_especiais_dict.items():
            self.__dados = self.__dados.replace(especial, letra)
        
    def removeLetrasAlfabeto(self) -> None:
        for caracter in self.__letras_alfabeto:
            self.__dados = self.__dados.replace(caracter, "")
    
    def getDados(self) -> str:
        return self.__dados
