# Quiz, Jan 27
user_input = input("Give me a number between 1 and 100: ") # just make up a number, assume it is an integer
print("You gave:", user_input)
print("Now watch this:")
tens = int(user_input) // 10
ones = int(user_input) % 10
print("There are", tens, "tens and", ones, "ones in", user_input)
ones = tens
tens = ones
print("Now we have", tens, "and", ones)


# Quiz, Jan 29
def my_favorite_math():
  x = 10
  y = 22
  z = y / x
  w = y // x

  a = z == w
  b = x < y and z < w
  if a or b:
    print("wow, you like this math, too?")
  elif a:
    print("i love this math!")
  else:
    print("i think i did something wrong.")

my_favorite_math()
    
