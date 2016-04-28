lister = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_number(lister):
    listbox = []
    for n in lister:
        if n % 2 == 0:
            listbox.append(n)
    return listbox

print(even_number(lister))
