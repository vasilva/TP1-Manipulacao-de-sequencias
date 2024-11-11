from lzw import *


def str_to_bin(s: str):
    """
    Converte uma string em ASCII para uma string binária.

    Args:
        s (str): A string a ser convertida.

    Returns:
        bin (str): A string binária.
    """
    bin = ""
    for c in s:
        bin += format(ord(c), "b").zfill(8)
    return bin


def bin_to_str(bin: str):
    """
    Converte uma string binária para uma string em ASCII.

    Args:
        bin (str): A string binária a ser convertida.

    Returns:
        s (str): A string em ASCII.
    """
    s = ""
    for i in range(0, len(bin), 8):
        s += chr(int(bin[i : i + 8], 2))
    return s


def compress(codes_list: list[int], max_bits: int = None) -> tuple[str, int]:
    """
    Comprime uma lista de códigos.

    Args:
        codes_list (list[int]): A lista de códigos.
        max_bits (int): O número máximo de bits.
        Se None, o número máximo de bits é calculado automaticamente.

    Returns:
        bin (str): A string binária compacta.
        max_bits (int): O número máximo de bits.
    """
    if max_bits == None:
        max_bits = max(codes_list).bit_length()
    bin = ""
    for i in codes_list:
        bin += format(i, "b").zfill(max_bits)
    return bin, max_bits


def decompress(bin: str, n_bits: int) -> list[int]:
    """
    Descomprime uma string binária.

    Args:
        bin (str): A string binária a ser descompactada.
        n_bits (int): O número de bits por código.

    Returns:
        codes_list (list[int]): A lista de códigos.
    """
    codes_list = []
    for i in range(0, len(bin), n_bits):
        codes_list.append(int(bin[i : i + n_bits], 2))
    return codes_list


def encoder(text: str, by: str = "binary") -> tuple[str, int]:
    """
    Compacta um texto.

    Args:
        text (str): Texto a ser compactado.
        by (str): 'binary' ou 'ascii'

    Returns:
        compressed (str): Texto compactado
        n_bits (int): O número de bits.
    """
    print(f"Encoding {by} text...")
    encoder = LZW_Encoder(by=by)
    t = text
    if by == "binary":
        t = str_to_bin(t)

    encoded = encoder.encode(t)
    compressed, n_bits = compress(encoded)
    print(f"Original Size:     {len(text)*8} bits")
    print(f"Compressed Size:   {len(compressed)} bits")
    print(f"Compression Ratio: {len(text)*8/len(compressed)}")
    return compressed, n_bits


def decoder(codes: str, n_bits: int, by: str = "binary") -> str:
    """
    Descompacta um texto.

    Args:
        codes (str): Texto compactado.
        n_bits (int): Número de bits por código.
        by (str): 'binary' ou 'ascii'

    Returns:
        decoded (str): Texto descompactado.
    """
    print(f"Decoding {by} text...")
    decoder = LZW_Decoder(by=by)
    c = decompress(codes, n_bits)
    decoded = decoder.decode(c)
    if by == "binary":
        decoded = bin_to_str(decoded)
    print(f"Compressed Size:   {len(codes)} bits")
    print(f"Original Size:     {len(decoded)*8} bits")
    print(f"Compression Ratio: {(len(decoded)*8)/len(codes)}")
    return decoded
