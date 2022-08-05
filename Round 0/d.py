def get_initial_rivers(system):
    n = int(input())
    for i in range(n - 1):
        r1, r2 = input().split()
        system[r1] = [r2]
    
    r0 = input()
    system[r0] = ['SEA']

def get_final_rivers(system):
    e = int(input())
    for i in range(e):
        r1, r2 = input().split()
        system[r1].append(r2)
        for river in system:
            if river != r1:
                system[river].append(system[river][i])

def can_reach(system, r1, r2, t):
    queue = [r1]
    while queue:
        source = queue.pop()
        if source == r2:
            return True
        if source == 'SEA':
            break
        queue.append(system[source][t])
    return False

if __name__ == '__main__':
    system = dict()
    get_initial_rivers(system)
    get_final_rivers(system)

    q = int(input())
    for i in range(q):
        t, r1, r2 = input().split()
        print('Yes' if can_reach(system, r1, r2, int(t)) else 'No')