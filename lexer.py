from mtoken import Token, TokenType

WHITESPACE = '\n\t '  # Добавляем пробел в список символов, которые игнорируются
DIGITS = '0123456789'

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char is not None:
            if self.current_char in WHITESPACE:
                self.advance()  # Просто игнорируем пробелы
            elif self.current_char in DIGITS or self.current_char == '.':
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"Illegal character '{self.current_char}'")

    def generate_number(self):
        number_str = ''
        decimal_point_count = 0

        while self.current_char is not None and (self.current_char in DIGITS or self.current_char == '.'):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break 
            number_str += self.current_char
            self.advance()

        return Token(TokenType.NUMBER, float(number_str))
