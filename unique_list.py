def unique_list(lister):
  x = []
  for a in lister:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5]))
