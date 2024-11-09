# Trabalho Prático I - Manipulação de Sequências
## Vinícius Alexandre da Silva

> Esse projeto faz a codificação de arquivos de texto usando o algoritmo Lempel-Ziv-Welch (LZW) e o uso de árvores Trie como estrutura de dados.

## Arquivos
1.  [lzw.py](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/blob/main/lzw.py): Contém o codificador e decodificador nas classes `lzw_encoder`e `lzw_decoder`, ambos criam um dicionário que relaciona substrings com inteiros.
* O `encoder` lê um texto em ASCII ou uma string binária e cria uma lista de inteiros, que são os códigos.
* Esses códigos são a entrada para o `decoder` que os convertem para a string original do texto.
2.  [trie.py](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/blob/main/trie.py): A estrutura de dados para a criação do dicionário. O tipo de árvore é a `RadixTree` ou árvore Trie compacta.
  
![Exemplo de Radix Tree](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/blob/main/baixados.png)

3. [functions.py](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/blob/main/Str_functions.py): Um conjunto de funções auxiliares como conversão de String em ASCII para string binária, compressão e descompressão da lista de códigos de inteiro para binário.
4. Na pasta [tests](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/tree/main/tests) há um conjunto de arquivos de entrada para a realização de testes.
5. E na pasta [encoded](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/tree/main/encoded) contém os resultados dos testes feitos, que contém:
* A lista de códigos, tanto como lista de inteiros e um número binário;
* A quantidade de bits por código usado;
* A comparação do tamanho do arquivo original e o tamanho comprimido, além da taxa de compressão.
