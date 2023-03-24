def count_ones(n: int, l: int, r: int) -> int:
    queue = [n]
    idx = 0

    while idx < len(queue):
        x = queue[idx]
        x_half = x // 2
        x_mod_2 = x % 2

        if x_half != 0:
            queue[idx : idx + 1] = [x_half, x_mod_2, x_half]
        else:
            idx += 1
    print(queue)
    ones_count = queue[l - 1 : r].count(1)
    return ones_count

# Example usage:
n = 10
l = 2
r = 4
print(count_ones(n, l, r))
