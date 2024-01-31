def happyLadybugs(b):
    # Return no immediately if there is only one or none bug
    if len(b) < 1:
        return 'NO'
    
    # Return yes immediately if there is no bug
    if len(b) == 1 and b[0] == '_':
        return 'YES'

    items = {}
    for bug in b:
        if bug not in items.keys():
            items[bug] = 1
        else:
            items[bug] += 1
    
    # Pop underscore in items map
    underscores = items.pop('_', 0)
        
    # If there is a lonely bug
    if 1 in items.values():
        print(items)
        print('Lonely~ I"m so lonely')
        return 'NO'
    
    if underscores > 0:
        return 'YES'
    
    # If there is no underscores
    length = len(b) - underscores
    for i in range(1, length - 1):
        if b[i] != b[i-1] and b[i] != b[i+1]:
            return 'NO'
        
    return 'YES'
