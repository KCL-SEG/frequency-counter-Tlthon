"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items :list[any]):
    freq:dict[any] = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    # Your code goes here
    return freq
