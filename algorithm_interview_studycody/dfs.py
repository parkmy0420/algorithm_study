graph = {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3]}

def recursive_dfs(v, discovered=[]):    # 재귀를 이용한 DFS 구현
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered
print(recursive_dfs(1))

# def stack_dfs(start_v): # 스택을 이용한 DFS 구현
#     discovered = []
#     stack = [start_v]
#     while stack:
#         v = stack.pop()
#         if v not in discovered:
#             discovered.append(v)
#             for w in graph[v]:
#                 stack.append(w)
#     return discovered
#
# print(stack_dfs(1))