# Trabalho Prático I - Manipulação de Sequências
## Vinícius Alexandre da Silva

> Esse projeto faz a codificação de arquivos de texto usando o algoritmo Lempel-Ziv-Welch (LZW) e o uso de árvores Trie como estrutura de dados.

## Arquivos
1.  [lzw.py](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/blob/main/lzw.py): Contém o codificador e decodificador nas classes `lzw_encoder`e `lzw_decoder`, ambos criam um dicionário que relaciona substrings com inteiros.
* O `encoder` lê um texto em ASCII ou uma string binária e cria uma lista de inteiros, que são os códigos.
* Esses códigos são a entrada para o `decoder` que os convertem para a string original do texto.
2.  [trie.py](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/blob/main/trie.py): A estrutura de dados para a criação do dicionário. O tipo de árvore é a `RadixTree` ou árvore Trie compacta.
  
![Exemplo de Radix Tree](https://github.com/vasilva/TP1-Manipulacao-de-sequencias/blob/main/baixados.png)



