# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    a = input()

    b = a.split()

    for symbol in b:
        c = ord(symbol)
        print(f"Код символа {symbol} равен {c}")
  

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
