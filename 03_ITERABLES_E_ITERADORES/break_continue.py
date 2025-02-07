nombres = ["Annie", "Lucia", "Hollman"]

for elemento in nombres:
    if elemento == "Lucia":
        break
    print(elemento)
    
for elemento in nombres:
    if elemento == "Lucia":
        continue
    print(elemento)
    
for elemento in nombres:
    print(elemento)
    break

for elemento in nombres:
    print(elemento)
    continue