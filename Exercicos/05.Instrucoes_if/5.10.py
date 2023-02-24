current_users = ['ADMIN', 'carolina', 'aurora', 'eva', 'philipe', 'matheos']
new_users = ['admin', 'carol', 'bruno', 'luna', 'philipe', 'marcos']

for new_user in new_users:
    if new_user in current_users or new_user.upper() in current_users:
        print("Forneca outro nome diferente de " + new_user + ".")
    else:
        print("Este nome " + new_user + " de usuario esta disponível.")