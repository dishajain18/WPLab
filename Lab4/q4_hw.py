class ParenthesesValidator:
    def is_valid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map.values():  # If it's an opening bracket
                stack.append(char)
            elif char in bracket_map.keys():  # If it's a closing bracket
                if not stack or stack.pop() != bracket_map[char]:
                    return False  # Mismatched or unbalanced bracket
            else:
                return False  # Invalid character

        return not stack  # Stack should be empty if valid


# Example usage
validator = ParenthesesValidator()
test_strings = ["()", "()[]{}", "(]", "({[)]", "{{{"]
for s in test_strings:
    print(f"{s}: {validator.is_valid(s)}")
