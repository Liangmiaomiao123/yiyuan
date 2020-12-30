#读取文件内容
with open(r'C:\Users\Lenovo\Desktop\text.txt','r') as file:
    print(file.read())


with open('text1.txt','a',encoding='utf-8')as file:
    b=file.write('长')
   
    print(b)