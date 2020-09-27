"""
A language pack defines all the alphabets in a particular natural
human language (e.g. English), as well as outlines rules guiding
which phonemes may replace each other. Feel free to create your
own language packs. Data Scrambler will use the rules you set to
replace consonants and vowels.

:author Benjamin Ayangbola
"""

phonemes = {
    # Dictionary of consonants in English language
    "consonants": {
        "b": ["p", "t", "d", "k", "g"],
        "p": ["b", "t", "d", "k", "g"],
        "t": ["p", "b", "d", "k", "g"],
        "d": ["p", "t", "b", "k", "g"],
        "k": ["p", "t", "d", "b", "g"],
        "g": ["p", "t", "d", "k", "b"],
        # Fricatives
        "f": ["v", "th", "s", "z", "sh", "h"],
        "th": ["v", "f", "s", "z", "sh", "h"],
        "s": ["v", "th", "s", "z", "sh", "h"],
        "z": ["v", "th", "s", "f", "sh", "h"],
        "sh": ["v", "th", "s", "z", "f", "h"],
        "h": ["v", "th", "s", "z", "sh", "f"],
        # Affricates
        "ch": ["v", "th", "s", "z", "f"],
        "j": ["ch", "v", "th", "s", "z", "f"],
        # Nasals
        "m": ["n"],
        "n": ["m"],
        # Laterals
        "l": ["l"],
        # Approximant
        "w": ["r", "y"],
        "r": ["w", "y"],
        "y": ["r", "w"]
    },
    # Dictionary of vowels in English language
    "vowels": {
        "a": ["e", "i", "o", "u"],
        "e": ["a", "i", "o", "u"],
        "i": ["e", "a", "o", "u"],
        "o": ["e", "i", "a", "u"],
        "u": ["e", "i", "o", "a"]
    }
}

phonemes['all'] = {**phonemes['consonants'], **phonemes['vowels']}
