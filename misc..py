def fib(n):
    if (n==0 or n==1):
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def pascal_triangle(n):
    line = []           
    if n==0:
        return [1]      #first line of Pascal triangle
    elif n==1:
        return [1,1]    #second line
    else:               #n-th line else
        line = [1] + [pascal_triangle(n-1)[i]+ pascal_triangle(n-1)[i+1] for i in range(len(pascal_triangle(n-1))-1)] + [1]
        return line


  
        
        


    
