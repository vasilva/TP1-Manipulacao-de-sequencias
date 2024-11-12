from trie import RadixTree


class LZW_Encoder:
    """
    LZW encoder.
    """

    def __init__(self, by: str = "ascii") -> None:
        """
        Cria um encoder de LZW.

        Args:
            by (str): O tipo de formato. Pode ser 'ascii' ou 'binary'.
        """
        self.next_code = 0
        self.dictionary = RadixTree()
        if by == "binary":
            self.add_to_dictionary("0")
            self.add_to_dictionary("1")
        else:
            for i in range(256):
                self.add_to_dictionary(chr(i))

    def add_to_dictionary(self, word: str) -> None:
        """
        Adiciona uma string ao dicionário.

        Args:
            word (str): A string a ser adicionada.
        """
        self.dictionary += word
        self.next_code += 1

    def encode(self, word: str, verbose: bool = False) -> list[int]:
        """
        Codifica uma string.

        Args:
            word (str): A string a ser codificada.
            verbose (bool): Se True, imprime os valores adicionados.

        Returns:
            r (list[int]): A lista de códigos.
        """
        r = []
        buffer = ""
        for i in range(len(word)):
            c = word[i]
            if len(buffer) == 0 or (buffer + c) in self.dictionary:
                buffer += c
            else:
                code = self.dictionary[buffer]
                self.add_to_dictionary(buffer + c)
                if verbose:
                    print("added:", buffer + c, "code:", self.next_code - 1)
                buffer = c
                r.append(code)
        if buffer:
            r.append(self.dictionary[buffer])

        return r


class LZW_Decoder:
    """
    LZW decoder.
    """

    def __init__(self, by: str = "ascii") -> None:
        """
        Cria um decoder de LZW.

        Args:
            by (str): O tipo de formato. Pode ser 'ascii' ou 'binary'.
        """
        self.next_code = 0
        self.dictionary = {}
        if by == "binary":
            self.add_to_dictionary("0")
            self.add_to_dictionary("1")
        else:
            for i in range(256):
                self.add_to_dictionary(chr(i))

    def add_to_dictionary(self, word: str) -> None:
        """
        Adiciona uma string ao dicionário.

        Args:
            word (str): A string a ser adicionada.
        """
        self.dictionary[self.next_code] = word
        self.next_code += 1

    def decode(self, symbols: list[int], verbose=False) -> str:
        """
        Decodifica uma lista de códigos.

        Args:
            symbols (list[int]): A lista de códigos.
            verbose (bool): Se True, imprime os valores adicionados.

        Returns:
            r (str): A string decodificada.
        """
        last_symbol = symbols[0]
        r = self.dictionary[last_symbol]

        for symbol in symbols[1:]:
            if symbol in self.dictionary.keys():
                current = self.dictionary[symbol]
                previous = self.dictionary[last_symbol]
                to_add = current[0]
                self.add_to_dictionary(previous + to_add)
                if verbose:
                    print("added:", previous + to_add, "code:", self.next_code - 1)
                r += current
            else:
                previous = self.dictionary[last_symbol]
                to_add = previous[0]
                self.add_to_dictionary(previous + to_add)
                if verbose:
                    print("added:", previous + to_add, "code:", self.next_code - 1)
                r += previous + to_add
            last_symbol = symbol
        return r
