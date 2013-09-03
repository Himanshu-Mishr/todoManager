def counter():
  f = open('data.todo','r')
  count = 0
  while f.readline():
    count += 1
  print(count)
  #return count

if __name__ == '__main__':
  counter()