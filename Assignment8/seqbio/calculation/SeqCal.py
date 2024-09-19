import re

def countBase(seq, base): 
    """
    This function counts the number of occurrences of a specific base in a given DNA sequence.
    
    Parameters:
    seq (str): The DNA sequence in which to count the base (e.g., "ATGC").
    base (str): The base to count within the sequence (e.g., "A").
    
    Returns:
    int: The number of times the specified base appears in the sequence.
    """
    return seq.count(base)

def gcContent(seq): 
    """
    This function calculates the GC content of a DNA sequence.
    
    The GC content is the percentage of nucleotides in the sequence that are either 
    guanine (G) or cytosine (C). It is calculated as:
    
    GC Content = (Number of G + Number of C) / (Total Number of Bases) * 100
    
    Parameters:
    seq (str): The DNA sequence for which to calculate GC content (e.g., "ATGC").
    
    Returns:
    float: The GC content as a percentage of the total sequence length.
    """
    g_count = countBase(seq, 'G')
    c_count = countBase(seq, 'C')
    total_bases = len(seq)
    gc_content = ((g_count + c_count) / total_bases) 
    # G+C/(A+T+G+C)
    # use countBase function to count bases
    return gc_content

def atContent(seq): 
    """
    This function calculates the AT content of a DNA sequence.
    
    The AT content is the percentage of nucleotides in the sequence that are either 
    adenine (A) or thymine (T). It is calculated as:
    
    AT Content = (Number of A + Number of T) / (Total Number of Bases) * 100
    
    Parameters:
    seq (str): The DNA sequence for which to calculate AT content (e.g., "ATGC").
    
    Returns:
    float: The AT content as a percentage of the total sequence length.
    """
    a_count = countBase(seq, 'A')
    t_count = countBase(seq, 'T')
    total_bases = len(seq)
    at_content = ((a_count + t_count) / total_bases) 
    # A+T/(A+T+G+C)
    # use countBase function to count bases
    return at_content

def countBasesDict(seq): 
    """
    Counts the occurrences of each nucleotide base in a given DNA sequence.

    Parameters:
    seq (str): The DNA sequence to be analyzed. The sequence should consist of characters representing nucleotide bases (e.g., 'A', 'T', 'C', 'G').

    Returns:
    dict: A dictionary where the keys are the nucleotide bases and the values are the counts of each base in the sequence.

    Example:
    >>> countBasesDict("ATCGATCGA")
    {'A': 3, 'T': 2, 'C': 2, 'G': 2}
    """
    basesM = {}
    for base in seq:
        if base in basesM:
            basesM[base] += 1
        else:
            basesM[base] = len(base)
    return basesM


