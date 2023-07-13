__all__ = ["is_under_attack", "is_valid_board"]


def is_under_attack(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return True
    return False


def is_valid_board(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_under_attack(queens[i][0], queens[i][1], queens[j][0], queens[j][1]):
                return False
    return True


queens = []
for i in range(8):
    x, y = map(int, input().split())
    queens.append((x, y))

if is_valid_board(queens):
    print("Ферзи не бьют друг друга")
else:
    print("Ферзи бьют друг друга")
