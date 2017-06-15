
# coding: utf-8

# In[34]:

def pole(i, j):
    result = "x"
    result += str(i)
    result += "_"
    result += str(j)
    return result

def hetmani(n):
    
    result = "Maximize \nobj: "
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += pole(i, j)
            if(not(i == n and j == n)):
                result += " + "
            else:
                result += "\n"
                
                

    result += "Subject to \n"
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += pole(i, j)
            if(not(j == n)):
                result += " + "
            else:
                result += " <= 1\n"
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += pole(j, i)
            if(not(j == n)):
                result += " + "
            else:
                result += " <= 1\n" 
                
                
    
    for i in range(-n + 1, n):
        if (i <= 0):
            for j in range(1, n+i+1):
                result += pole(j, j - i)
                if (j != n+i):    
                    result += " + "
        else:
            for j in range(i + 1, n + 1):
                result += pole(j, j-i)
                if (j != n):
                    result += " + "  
        result += " <= 1\n"
    for i in range(-n+1, n):
        if (i <= 0):
            for j in range(1, n+i+1):
                result += pole(j, i-j+n+1)
                if (j != n+i):    
                    result += " + "
        else:
            for j in range(i + 1 , n + 1):
                result += pole(j, i-j+n+1)
                if (j != n):
                    result += " + "  
        result += " <= 1\n"
        
        
    #wartosci
    result += "Bounds \n"
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += "0 <= "
            result += pole(i, j)
            result += " <= 1\n"
            
    #nazwy zmiennych
    result += "Generals \n"
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += pole(i, j)
            result += "\n"
    result += "End"
    return result

n = int(input("Rozmiar szaczownicy: "))
print(hetmani(n))

# In[16


# In[ ]:



