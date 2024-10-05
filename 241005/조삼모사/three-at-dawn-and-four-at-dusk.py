n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

def combinations(arr, r):
    pool = tuple(arr)
    n = len(pool)
    
    def recursive_combinations(start, combo):
        if len(combo) == r:
            yield tuple(combo)
        else:
            for i in range(start, n):
                combo.append(pool[i])
                yield from recursive_combinations(i + 1, combo)
                combo.pop()
    
    return recursive_combinations(0, [])

def get_mornings(arr):
    return combinations(arr,n//2)

def get_afternoon(arr, morning):
    return [i for i in arr if i not in morning]

def get_delta(matrix,morning,afternoon):
    morning_sum = 0
    for i in range(len(morning)):
        for j in range(len(morning)):
            a,b = morning[i],morning[j]
            morning_sum += (matrix[a][b] + matrix[b][a])
    afternoon_sum = 0
    for i in range(len(afternoon)):
        for j in range(len(afternoon)):
            c,d = afternoon[i],afternoon[j]
            afternoon_sum += (matrix[c][d] + matrix[d][c])
    return abs(afternoon_sum - morning_sum)//2

arr = list(range(n))
mornings = get_mornings(arr)
delta_list = []
for m in mornings:
    a = get_afternoon(arr, m)
    delta_list.append(get_delta(matrix,m,a))
print(min(delta_list))