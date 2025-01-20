from lexer import Lexer
from parser import Parser

while True:
    text = input("calc > ")
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    print(list(tokens))  # Выводим токены для диагностики
    parser = Parser(tokens)
    tree = parser.parser()  # Используем метод экземпляра
    print(tree)
