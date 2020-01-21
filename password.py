password='a123456'
i=3
while True:
    pwd=input('enter the password:')
    if pwd=='a123456':
        print('correct')
        break
    else:
        i=i-1
        print('wrong',i,'chance left')
        if i==0:
            break



