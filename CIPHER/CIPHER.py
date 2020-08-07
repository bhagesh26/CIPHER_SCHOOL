def balance(s):
    a=[]
    for i in s:
        if i in ['{','(','[']:
            a.append(i)
        else:
            if not a:
                return False
            current=a.pop()
            print(current)
            
            if current=='(':
                if i != ')':
                    return False
            if current=='[':
                if i != ']':
                    return False
            if current=='{':
                if i != '}':
                    return False
    if a:
        return False
    return True                    


for t in range(int(input())):
    s=input()
    
    
    
                    
    if balance(s):
        print('Yes')                                       
    else:
        print('NO')     

