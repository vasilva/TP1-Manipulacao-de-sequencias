from lzw import *


def compress(codes_list, max_bits=None):
    """
    Comprime uma lista de códigos.

    Args:
        codes_list: A lista de códigos.
        max_bits: O número máximo de bits.
        Se None, o número máximo de bits é calculado automaticamente.

    Returns:
        bin: A string binária compacta.
        max_bits: O número máximo de bits.
    """
    if max_bits == None:
        max_bits = max(codes_list).bit_length()
    bin = ""
    for i in codes_list:
        bin += format(i, "b").zfill(max_bits)
    return bin, max_bits


def decompress(bin, n_bits):
    """
    Descomprime uma string binária.

    Args:
        bin: A string binária a ser descompactada.
        n_bits: O número de bits por código.

    Returns:
        codes_list: A lista de códigos.
    """
    codes_list = []
    for i in range(0, len(bin), n_bits):
        codes_list.append(int(bin[i : i + n_bits], 2))
    return codes_list


def encoder(text):
    """
    Compacta um texto.

    Args:
        text: Texto a ser compactado.

    Returns:
        compressed: Texto compactado
        n_bits: O número de bits.
    """
    print(f"Encoding text...")
    encoder = LZW_Encoder()
    t = text

    encoded = encoder.encode(t)
    compressed, n_bits = compress(encoded)
    print(f"Original Size:     {len(text)*8} bits")
    print(f"Compressed Size:   {len(compressed)} bits")
    print(f"Compression Ratio: {len(text)*8/len(compressed)}")
    return compressed, n_bits


def decoder(codes, n_bits):
    """
    Descompacta um texto.

    Args:
        codes: Texto compactado.
        n_bits: Número de bits por código.

    Returns:
        decoded: Texto descompactado.
    """
    print(f"Decoding text...")
    decoder = LZW_Decoder()
    c = decompress(codes, n_bits)
    decoded = decoder.decode(c)

    print(f"Compressed Size:   {len(codes)} bits")
    print(f"Original Size:     {len(decoded)*8} bits")
    print(f"Compression Ratio: {(len(decoded)*8)/len(codes)}")
    return decoded
