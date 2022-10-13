"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items :list):
    freq:dict[any] = {}
    for item in items:
        str_item = str(item)
        freq[str_item] = freq.get(str_item, 0) + 1
    # Your code goes here
    return freq
