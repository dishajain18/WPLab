class StringReverser:
    def reverse_words(self, s: str) -> str:
        return " ".join(s.split()[::-1])  # Split, reverse, and join back

# Example usage
reverser = StringReverser()
str = input("Enter a sentence: ")
print(f"Reversed: {reverser.reverse_words(str)}")
