import random

def start_boats_position(how_many_boats):
    n1, n2 = how_many_boats
    board = [[" " for _ in range(4)] for _ in range(4)]
    boats = []

    def is_valid_position(position):
        x, y = position
        if x < 0 or x >= 4 or y < 0 or y >= 4 or board[x][y] != " ":
            return False
        
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < 4 and ny >= 0 and ny < 4 and board[nx][ny] != " ":
                    return False
        
        return True

    def place_boat(boat):
        for position in boat:
            x, y = position
            board[x][y] = "X"

    # ставим двупалубный корабль
    if 1 >= n2 > 0:
        placed = False
        for _ in range(100):  #  Добавление ограничения, чтобы избежать бесконечного цикла
            letter = random.choice(["a", "b", "c"])
            number = random.randint(1, 3)
            x = ord(letter) - 97
            y = number - 1
            if is_valid_position((x, y)) and is_valid_position((x+1, y)):
                place_boat([(x, y), (x+1, y)])
                boats.append([(letter, number), (chr(ord(letter) + 1), number)])
                placed = True
                break
        if not placed:
            return None  # Возвращайте None, если не удалось разместить лодку в течение 100 попыток

    # Pставим однопалубный корабль
    for _ in range(n1):
        placed = False
        for _ in range(100):  #  Добавление ограничения, чтобы избежать бесконечного цикла
            letter = random.choice(["a", "b", "c", "d"])
            number = random.randint(1, 4)
            x = ord(letter) - 97
            y = number - 1
            if is_valid_position((x, y)):
                place_boat([(x, y)])
                boats.append([(letter, number)])
                placed = True
                break
        if not placed:
            return None  # Возвращайте None, если не удалось разместить лодку в течение 10 попыток

    return boats

# пример
boats = start_boats_position((3, 1))
if boats is not None:
    print(boats)
else:
    print("Не удалось разместить лодки в течение указанного количества попыток.")