def gridSearch(G, P):
    rows = len(P)
    cols = len(P[0])
    
    result = 'NO'
    
    for i in range(len(G)):
        
        # Search every cell in a row
        fi = 0
        li = fi + cols
        
        while li < len(G[i]) + 1:
            
            # Explore all column
            if G[i][fi:li] == P[0]:
                result = 'YES'
                print('FOUND in G:', G[i][fi:li])
                
                for j in range(1, len(P) + 1):
                    # Prevent error if the index is out of limit
                    if (i + j) >= len(G):
                        break

                    print('Checking', G[i+j][fi:li], P[j])
                       
                    if G[i+j][fi:li] == P[j]:
                        result = 'YES'
                    else:
                        result = 'NO'
                        break
            
            if result == 'YES':
                return result
            
            fi += 1
            li = fi + cols
        pass
    pass
    
    return result


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)
        print(result)
