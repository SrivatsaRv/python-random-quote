import random
def primary():


  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 18
  rnd = random.randint(0,last)
  print(quotes[rnd])
  print(quotes[rnd+1])
  print(quotes[rnd+2])

if __name__== "__main__":
  primary()
