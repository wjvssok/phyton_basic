def form_list(N, K):
    krug = list(range(1, N + 1))
    result = []  
    idx = 0
    while len(krug) > 0:
        idx = (idx + K - 1) % len(krug)
        
        result.append(krug[idx])
        
        krug.pop(idx)

    return result
    
N = int(input())
K = int(input())
print(form_list(N, K))