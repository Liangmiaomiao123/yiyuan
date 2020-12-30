d={"a":1,"b":2,"c":3}
for e in d:
    print(e)

#迭代key值
for k in d:
    print(k,':',d[k])

#同时迭代key,value
# for k,v in d:
#     print(k,':',v)

#迭代value:
for v in d.values():
    print(v)

#获取迭代索引及元素
l=[3,5,6,2,1]
for i,v in enumerate(l):
    print(i,':',v)

#列表生成式
m=list(range(10))
print(m)

l=[4,6,43,2,8]
p=[x*x for x in l]
print(p)

r=[x+y for x in "abc" for y in "xyz"]
print(r)

  

# g=(x*x for x in range(101))
# print(g)
# print(next(g))
# print(next(g))
# b=lambda x:x*x
# print(b(5))
# def f(x):
    
#     print(list(map(f,[1,2,3])))


#求x的n次方
def power2(x,n=2):
    s=1
    while n>0:
        s*=x
        n=n-1
        return s
    print(power2(3,4))
l=[1,2,3,4,5,6,7]
m=l[0:4]
# print(m)
print(l[4:7])
print(l[:-1])

#元祖使用切片
t=tuple(range(100))
print(t)
print(t[10:30])

print(list(map(str,range(10))))