def find_combinations(n, coins, index=0, current_combination=None):
    if current_combination is None:
        current_combination = []

    if n == 0:
        print(current_combination)
        return

    if index >= len(coins):
        return

    coin = coins[index]
    max_count = n // coin

    for count in range(max_count + 1):
        find_combinations(n - coin * count, coins, index + 1, current_combination + [count])

# Example usage
n = 10  # Replace this with any amount
coins = [500, 100, 10, 5, 1]
find_combinations(n, coins)
