import math
import random


def cost(board):
    """Number of attacking pairs of queens. board[col] = row."""
    n = len(board)
    conflicts = 0
    for c1 in range(n):
        for c2 in range(c1 + 1, n):
            r1, r2 = board[c1], board[c2]
            if r1 == r2 or abs(r1 - r2) == abs(c1 - c2):
                conflicts += 1
    return conflicts


def neighbor(board):
    """Pick a random column and move its queen to a different random row."""
    n = len(board)
    new_board = board[:]
    c = random.randrange(n)
    new_row = random.choice([r for r in range(n) if r != board[c]])
    new_board[c] = new_row
    return new_board, c


def print_board(board):
    n = len(board)
    for r in range(n):
        print(" ".join("Q" if board[c] == r else "." for c in range(n)))


def simulated_annealing(board, T, alpha, T_min, max_iter, verbose=False):
    current = board[:]
    current_cost = cost(current)
    best, best_cost = current[:], current_cost

    for it in range(1, max_iter + 1):
        if current_cost == 0 or T < T_min:
            break

        proposed, col = neighbor(current)
        proposed_cost = cost(proposed)
        delta = proposed_cost - current_cost

        if delta < 0:
            accept, P, R = True, 1.0, None
        else:
            P = math.exp(-delta / T)
            R = random.random()
            accept = R < P

        if verbose:
            print(f"Iter {it}: col {col} -> row {proposed[col]} | "
                  f"dE={delta:+d} | T={T:.4f}", end=" | ")
            if R is None:
                print("better move, ACCEPT")
            else:
                print(f"P={P:.3f}, R={R:.3f}, {'ACCEPT' if accept else 'REJECT'}")

        if accept:
            current, current_cost = proposed, proposed_cost
            if current_cost < best_cost:
                best, best_cost = current[:], current_cost

        T *= alpha  

    return best, best_cost, it


def main():
    n = 8

    T = float(input("Enter initial temperature (e.g. 10.0): ") or 10.0)
    alpha = float(input("Enter cooling factor alpha (e.g. 0.99): ") or 0.99)
    max_iter = int(input("Enter max iterations (e.g. 10000): ") or 10000)

    choice = input("Initial board: (1) diagonal [0..7], (2) random, "
                   "(3) enter manually? [1/2/3]: ").strip() or "1"
    if choice == "2":
        board = [random.randrange(n) for _ in range(n)]
    elif choice == "3":
        board = list(map(int, input("Enter 8 row values (0-7) separated by spaces: ").split()))
        if len(board) != n or any(r < 0 or r >= n for r in board):
            print("Invalid board. Using diagonal board.")
            board = list(range(n))
    else:
        board = list(range(n))

    show = input("Show step-by-step log? (y/n): ").strip().lower() == "y"
    T_min = 1e-6

    print(f"\nInitial board: {board} | Cost: {cost(board)}\n")

    restarts = 0
    while True:
        best, best_cost, iters = simulated_annealing(board, T, alpha, T_min, max_iter, show)
        if best_cost == 0:
            break
        restarts += 1
        if restarts > 50:
            break
        board = [random.randrange(n) for _ in range(n)]

    print("\n--- Result ---")
    print(f"Final board : {best}")
    print(f"Final cost  : {best_cost}")
    print(f"Restarts    : {restarts}")
    if best_cost == 0:
        print("Solution found!\n")
        print_board(best)
    else:
        print("No solution found. Try a higher temperature, alpha closer to 1, or more iterations.")


if __name__ == "__main__":
    main()
