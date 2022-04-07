def calc(st):
    from collections import deque
    my_stack = deque()
    st=st.split()
    for i in st:
        if i.isdigit():
            my_stack.append(i)
        else:
            a=my_stack.pop()
            b=my_stack.pop()
            my_stack.append(eval(f'{b}{i}{a}'))
    print(my_stack.pop())
    
def delimiter(st):
    my_stack = []
    st = st.replace(" ","")
    for i in st:
        n = len(my_stack)
        if i=="}" and my_stack[n-1]=="{":
            my_stack.pop()
        elif i==")" and my_stack[n-1]=="(":
            my_stack.pop()
        elif i=="]" and my_stack[n-1]=="[":
            my_stack.pop()
        else:
            my_stack.append(i)
    print(len(my_stack)==0)

def number(inp, outp):
    import os
    fname = inp
    if os.path.isfile(fname):
        lines=[]
        n=0
        with open(inp,'r', encoding='utf8') as f:
            for line in f:
              n+=1
              lines.append(str(n)+" "+line)
        with open(outp,'w',encoding='utf8') as f:
            for line in lines:
                f.write(line)
    else:
        print('no such file')
