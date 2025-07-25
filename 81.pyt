def find_paths(n, m):
    def dfs(x, y, path):
        if x == n - 1 and y == m - 1:
            paths.append(path)
            return
        if x < n - 1:
            dfs(x + 1, y, path + 'D')
        if y < m - 1:
            dfs(x, y + 1, path + 'R')

    paths = []
    dfs(0, 0, '')
    return paths

# Example usage:
n = 3  # number of rows
m = 3  # number of columns
results = find_paths(n, m)
for p in results:
    print(p)