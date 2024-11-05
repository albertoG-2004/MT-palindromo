class TuringMachine:
    def __init__(self, word):
        self.tape = list(word.upper())
        self.head = 0
        self.state = 'start'

    def is_palindrome(self):
        left = 0
        right = len(self.tape) - 1
        while left < right:
            if self.tape[left] != self.tape[right]:
                return False
            left += 1
            right -= 1
        return True