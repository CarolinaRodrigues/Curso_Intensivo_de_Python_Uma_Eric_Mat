users = ['ADMIN', 'carolina', 'aurora', 'eva', 'philipe', 'matheos']
#users = []
if users:
    for user in users:
        if user.upper() == 'admin' or user.title() == 'admin' or user.lower() == 'admin':
            print("\nOlá " + user + ", gostaria de ver um relatório de status?")
        else:
            print("\nOlá " + user + ", obrigado por fazer login novamente.") 
else:
    print("Precismaos encontrar alguns usuarios!")