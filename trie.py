class RadixTree:
    """
    Uma árvore de prefixos compacta.
    """

    def __init__(self) -> None:
        """
        Cria uma árvore de prefixos compacta vazia.
        >>> RadixTree()
        """
        # O nó raiz da árvore
        self.root = RadixNode()
        # O número de palavras na árvore
        self.size = 0
        # Próximo índice
        self.next_index = 0

    def insert(self, word: str) -> None:
        """
        Insere uma palavra na árvore.

        Args:
            word (str): palavra a ser inserida.

        >>> RadixTree().insert("word")
        """
        index = self.next_index
        self.root.insert(word, index)
        self.next_index += 1
        self.size += 1

    def insert_many(self, words: list[str]) -> None:
        """
        Insere várias palavras na árvore.

        Args:
            words (list[str]): lista de palavras a serem inseridas.

        >>> RadixTree().insert_many(["word1", "word2"])
        """
        for word in words:
            self.insert(word)

    def find(self, word: str) -> tuple[bool, int]:
        """
        Verifica se uma palavra está na árvore e retorna seu índice.

        Args:
            word (str): palavra a ser verificada.

        Returns:
            bool: True se a palavra estiver na árvore,
                  False caso contrário.
            int: Índice da palavra,
                 -1 caso a palavra não encontrada.

        >>> RadixTree().insert("word")
        >>> RadixTree().find("word")
        (True, 0)
        """
        return self.root.find(word)

    def index(self, word: str) -> int:
        """
        Retorna o índice de uma palavra na árvore.

        Args:
            word (str): palavra a ser verificada.

        Returns:
            int: índice da palavra na árvore.

        >>> RadixTree().insert("word")
        >>> RadixTree().index("word")
        0
        """
        return self.find(word)[1]

    def __getitem__(self, word: str) -> int:
        """
        Retorna o índice de uma palavra na árvore.

        Args:
            word (str): palavra a ser verificada.

        Returns:
            int: índice da palavra na árvore.

        >>> RadixTree().insert("word")
        >>> RadixTree()["word"]
        0
        """
        return self.index(word)

    def delete(self, word: str) -> bool:
        """
        Deleta uma palavra da árvore.

        Args:
            word (str): palavra a ser deletada.

        Returns:
            bool: True caso a palavra esteja na árvore e for deletada,
                  False caso a palavra não esteja na árvore.

        >>> RadixTree().insert("word")
        >>> RadixTree().delete("word")
        True
        """
        if self.root.delete(word):
            self.size -= 1
            return True
        return False

    def print_tree(self) -> None:
        """
        Imprime a árvore.

        >>> RadixTree().insert_many(["word1", "word2"])
        >>> RadixTree().print_tree()
        --- word
        ------ 1:   (0)
        ------ 2:   (1)
        """
        self.root.print_tree()

    def all_words(self) -> dict:
        """
        Retorna todas as palavras da árvore numa lista.

        Returns:
            list[(str, int)]: lista de palavras e índices.

        >>> RadixTree().insert_many(["word1", "word2"])
        >>> RadixTree().all_words()
        [('word1', 0), ('word2', 1)]
        """
        return self.root.all_words()

    def __repr__(self) -> str:
        """
        >>> RadixTree()
        'RadixTree(size=0)'
        """
        return f"RadixTree(size={self.size})"

    def __str__(self) -> str:
        """
        >>> RadixTree().insert_many(["word1", "word2"])
        >>> print(RadixTree())
        {'word1': 0, 'word2': 1}
        """
        return self.all_words().__str__()

    def __contains__(self, word: str) -> bool:
        """
        >>> RadixTree().insert("word")
        >>> "word" in RadixTree()
        True
        """
        return self.find(word)[0]

    def __iter__(self):
        """
        >>> RadixTree().insert_many(["word1", "word2"])
        >>> [(word, i) for (word, i) in RadixTree()]
        [('word1', 0), ('word2', 1)]
        """
        return iter(self.all_words())

    def __add__(self, word: str) -> None:
        """
        >>> RadixTree() + "word"
        >>> "word" in RadixTree()
        True
        """
        self.insert(word)

    def __iadd__(self, word: str):
        """
        >>> RadixTree() += "word"
        >>> "word" in RadixTree()
        True
        """
        self.insert(word)
        return self

    def __sub__(self, word: str) -> bool:
        """
        >>> RadixTree().insert("word")
        >>> RadixTree() - "word"
        >>> "word" not in RadixTree()
        True
        """
        return self.delete(word)

    def __isub__(self, word: str):
        """
        >>> RadixTree().insert("word")
        >>> RadixTree() -= "word"
        >>> "word" not in RadixTree()
        True
        """
        self.delete(word)
        return self

    def __len__(self) -> int:
        """
        >>> RadixTree().insert_many(["word1", "word2"])
        >>> len(RadixTree())
        2
        """
        return self.size

    def sort(self, by: str = "index") -> list[(str, int)]:
        """
        >>> RadixTree().insert_many(["word1", "word0"])
        >>> RadixTree().sort(by="index")
        [('word1', 0), ('word0', 1)]
        >>> RadixTree().sort(by="word")
        [('word0', 1), ('word1', 0)]
        """
        words = self.all_words()
        words = [(word, i) for word, i in words.items()]
        if by == "index":
            words.sort(key=lambda x: x[1])
        elif by == "word":
            words.sort(key=lambda x: x[0])
        return words


class RadixNode:
    """
    Um nó da árvore de prefixos compacta.
    """

    def __init__(
        self, prefix: str = "", is_leaf: bool = False, index: int = None
    ) -> None:
        """
        Cria um nó da árvore de prefixos compacta.

        Args:
            prefix (str): prefixo do nó.
            is_leaf (bool): se o nó é uma folha.
            index (int): índice da palavra adicionada

        >>> RadixNode()
        >>> RadixNode("prefix")
        """
        # Mapeamento a partir do primeiro caractere do prefixo do nó
        self.nodes: dict[str, RadixNode] = {}
        # Um nó será uma folha se a árvore conter sua palavra
        self.is_leaf = is_leaf
        self.prefix = prefix
        self.index = index

    def _match(self, word: str) -> tuple[str, str, str]:
        """
        Calcula a substring comum do prefixo do nó e uma palavra.

        Args:
            word (str): palavra para comparar.

        Returns:
            (str, str, str): substring comum, prefixo restante, palavra restante.

        >>> RadixNode("myprefix")._match("mystring")
        ('my', 'prefix', 'string')
        """
        x = 0
        for q, w in zip(self.prefix, word):
            if q != w:
                break

            x += 1

        return self.prefix[:x], self.prefix[x:], word[x:]

    def insert(self, word: str, index: int) -> None:
        # Caso 1: Se a palavra for o prefixo do nó
        # Solução: Definimos o nó atual como folha
        if self.prefix == word and not self.is_leaf:
            self.is_leaf = True

        # Caso 2: O nó não tem arestas que tenham um prefixo para a palavra
        # Solução: Criamos uma aresta do nó atual para um novo
        # contendo a palavra
        elif word[0] not in self.nodes:
            self.nodes[word[0]] = RadixNode(word, True, index)

        else:
            new_node = self.nodes[word[0]]
            substring, rest_prefix, rest_word = new_node._match(word)

            # Caso 3: O prefixo do nó é igual ao correspondente
            # Solução: Inserimos a palavra restante no próximo nó
            if rest_prefix == "":
                self.nodes[substring[0]].insert(rest_word, index)

            # Caso 4: A palavra é maior que a correspondência
            # Solução: Crie um nó entre os dois nós, altere
            # prefixos e adicione o novo nó para a palavra restante
            else:
                new_node.prefix = rest_prefix

                aux_node = self.nodes[substring[0]]
                self.nodes[substring[0]] = RadixNode(substring, False, index)
                self.nodes[substring[0]].nodes[rest_prefix[0]] = aux_node

                if rest_word == "":
                    self.nodes[substring[0]].is_leaf = True
                else:
                    self.nodes[substring[0]].insert(rest_word, index)

    def find(self, word: str) -> tuple[bool, int]:
        new_node = self.nodes.get(word[0], None)
        if not new_node:
            return (False, -1)
        else:
            substring, rest_prefix, rest_word = new_node._match(word)
            # Se houver prefixo restante, a palavra não pode estar na árvore
            if rest_prefix != "":
                return (False, -1)
            # Isso se aplica quando a palavra e o prefixo são iguais
            elif rest_word == "":
                return (True, new_node.index) if new_node.is_leaf else (False, -1)
            # Temos palavras restantes, então verificamos o próximo nó
            else:
                return new_node.find(rest_word)

    def delete(self, word: str) -> bool:
        new_node = self.nodes.get(word[0], None)
        if not new_node:
            return False
        else:
            substring, rest_prefix, rest_word = new_node._match(word)
            # Se houver prefixo restante, a palavra não pode estar na árvore
            if rest_prefix != "":
                return False, -1
            # Temos palavras restantes, então verificamos o próximo nó
            elif rest_word != "":
                return new_node.delete(rest_word)
            # Se não for uma folha, não precisamos excluir
            elif not new_node.is_leaf:
                return False
            else:
                # Excluímos os nós se nenhuma aresta sair deles
                if len(new_node.nodes) == 0:
                    del self.nodes[word[0]]
                    # Nós mesclamos o nó atual com seu único filho
                    if len(self.nodes) == 1 and not self.is_leaf:
                        merge_node = next(iter(self.nodes.values()))
                        self.is_leaf = merge_node.is_leaf
                        self.prefix += merge_node.prefix
                        self.index = merge_node.index
                        self.nodes = merge_node.nodes
                # Se houver mais de uma aresta, nós apenas a marcamos como não-folha
                elif len(new_node.nodes) > 1:
                    new_node.is_leaf = False
                # Se houver 1 aresta, nós a mesclamos com seu filho
                else:
                    merge_node = next(iter(new_node.nodes.values()))
                    new_node.is_leaf = merge_node.is_leaf
                    new_node.prefix += merge_node.prefix
                    new_node.index = merge_node.index
                    new_node.nodes = merge_node.nodes
                return True

    def print_tree(self, height: int = 0) -> None:
        if self.prefix != "":
            print(
                "---" * height,
                (
                    f"{self.prefix}:    ({self.index})"
                    if self.is_leaf
                    else f"{self.prefix}"
                ),
            )

        for value in self.nodes.values():
            value.print_tree(height + 1)

    def all_words(self) -> dict[int, str]:
        words = {}
        if self.is_leaf:
            words[self.prefix] = self.index
        for value in self.nodes.values():
            sufixes = value.all_words()
            for suffix, index in sufixes.items():
                words[self.prefix + suffix] = index
        return words
