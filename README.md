# Trabalho Prático I - Manipulação de Sequências
## Vinícius Alexandre da Silva

> Esse projeto faz a codificação de arquivos de texto usando o algoritmo Lempel-Ziv-Welch (LZW) e o uso de árvores Trie como estrutura de dados.

## Arquivos
1. [main.ipynb](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/blob/main/main.ipynb): Notebook principal contendo o fluxo principal de codificação e decodificação. O processo é o seguinte:
* Lê o arquivo de entrada da pasta [tests](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/tree/main/tests);
* Faz a codificação, calculando seu tempo de computação;
* Faz a comparação entre os tamanhos do arquivo original e o resultado comprimido, os cálculos de taxa de compressão e tempo relativo ao tamanho da entrada;
* Grava os resultados no arquivo [out.csv](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/tree/main/out.csv).

2.  [lzw.py](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/blob/main/lzw.py): Contém o codificador e decodificador nas classes `lzw_encoder`e `lzw_decoder`, ambos criam um dicionário que relaciona substrings com inteiros.
* O `encoder` lê um texto em ASCII ou uma string binária e cria uma lista de inteiros, que são os códigos.
* Esses códigos são a entrada para o `decoder` que os convertem para a string original do texto.

3.  [trie.py](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/blob/main/trie.py): A estrutura de dados para a criação do dicionário. O tipo de árvore é a `RadixTree` ou árvore Trie compacta.

![Exemplo de Radix Tree](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/blob/main/trie.png)

4. [functions.py](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/blob/main/Str_functions.py): Um conjunto de funções auxiliares como conversão de String em ASCII para string binária, compressão e descompressão da lista de códigos de inteiro para binário.

5. Na pasta [tests](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/tree/main/tests) há um conjunto de arquivos de entrada para a realização de testes.

6. E na pasta [encoded](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/tree/main/encoded) contém os resultados dos testes feitos, que contém:
* A lista de códigos, tanto como lista de inteiros e um número binário;
* A quantidade de bits por código usado;
* A comparação do tamanho do arquivo original e o tamanho comprimido, além da taxa de compressão.
