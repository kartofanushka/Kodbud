import time

def counter(s): # diffculty O(N**2)
    for let in s:
        count=0
        for sub_let in s:
            if let==sub_let:
                count +=1
        # print(let,count)
start=time.time()
for i in range (10_000):
    counter('aabbnnddmmtjjglsjh')
end=time.time()
print(end-start)
    
# set() уникальные эл-ты
def counter_new(s): # diffculty O(N*M)
    for let in set(s): #M число уник букв
        count=0
        for sub_let in s: #N число всех букв
            if let==sub_let:
                count +=1
        # print(let,count)
# худшая сложность , когда M=N

start=time.time()
for i in range (10_000):
    counter_new('aabbnnddmmtjjglsjh')
end=time.time()
print(end-start)

def counter_on(s): # O(N)
    let_counter={}
    for let in s:
        let_counter[let]=let_counter.get(let,0)+1
    # print(let_counter)
    
start=time.time()
for i in range (10_000):
    counter_on('aabbnnddmmtjjglsjh')
end=time.time()
print(end-start)
