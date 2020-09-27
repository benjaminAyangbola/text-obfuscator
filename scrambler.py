# Author: Benjamin Ayangbola
# Created: July 19, 2020; 10:20PM

# Standard library imports
from random import randint

# Local application imports
from language_packs.english import phonemes


class DataScrambler:
    """
    This data privacy protection tool obfuscates a text, but
    retains readability.
    """

    def __init__(self, language: str = 'english'):
        self._depth = 'shallow'
        """
        Define the depth of the scrambling operation as 'shallow'
        or 'deep'. Default depth is 'shallow' (for faster scrambling)
        """

        self.language = language
        """
        Set a language pack for replacing phonemes. If no language pack
        is specified, Data Scrambler defaults to language_packs.english
        """

    @property
    def depth(self) -> str:
        """ Get the depth property of this class """
        return self._depth

    @depth.setter
    def depth(self, value: str):
        """ Assign a value to the depth property of this class """
        self._depth = value

    def language(self) -> str:
        """ Get language of text to be scrambled from the specified language pack """
        return self.language

    def _get_replacement(self, phoneme: str) -> str:
        """ Replace a phoneme based on the specified language pack """
        if phoneme in phonemes['all']:
            # Get random replacement from list of possible replacements for phoneme
            possible_replacements = phonemes['all'][phoneme]
            max_index = len(possible_replacements) - 1
            index = randint(0, max_index)
            return possible_replacements[index]
        return phoneme

    def obfuscate(self, text: str) -> str:
        """ Scramble a unit of text """
        if self._depth == 'deep':
            return self._deep_scramble(text)
        else:
            return self._shallow_scramble(text)

    def _x(self, text: str) -> str:
        """
        Apply deep scrambling to a unit of text. Deep scrambling
        changes both vowels and consonants, randomly generating
        a replacement for each occurrence based on the rules
        defined in your language pack
        """
        new_text: str = ''
        # Separate all words in text so that unique phoneme replacement rules
        # can be applied to each
        words = text.split(' ')

        # Run self._replace() function on each character in words argument
        for word in words:
            scrambled_word = list(map(lambda phoneme: self._get_replacement(phoneme), word))
            # Flatten list into a string
            scrambled_word = ''.join(map(str, scrambled_word))
            new_text += (scrambled_word + ' ')
        return new_text.strip()

    def _deep_scramble(self, text: str) -> str:
        """
        Apply deep scrambling to a unit of text. Deep scrambling
        changes both vowels and consonants, randomly generating
        a replacement for each occurrence based on the rules
        defined in your language pack
        """
        # Replace all vowels
        new_text = self._shallow_scramble(text)
        # Replace all consonants
        for consonant in phonemes['consonants']:
            replacement = self._get_replacement(consonant)
            new_text = new_text.replace(consonant, replacement)
        return new_text

    def _shallow_scramble(self, text: str) -> str:
        """
        Apply shallow scrambling to a unit of text. Shallow scrambling
        changes only vowels. It will not replace upper case alphabets.
        """
        for vowel in phonemes['vowels']:
            replacement = self._get_replacement(vowel)
            text = text.replace(vowel, replacement)
        return text
