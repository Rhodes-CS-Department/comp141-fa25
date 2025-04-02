# Quiz 1, Jan 27
user_input = input("Give me a number between 1 and 100: ") # just make up a number, assume it is an integer
print("You gave:", user_input)
print("Now watch this:")
tens = int(user_input) // 10
ones = int(user_input) % 10
print("There are", tens, "tens and", ones, "ones in", user_input)
ones = tens
tens = ones
print("Now we have", tens, "and", ones)


# Quiz 2, Jan 29
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
    

# Quiz 3, Feb 3, 2025
def my_little_function(a, b, c):
  a = b + c
  c = 2 * a
  b = c / b
  print("little: ", a, b, c)

def my_big_function(a, b, c):
  a = a + b + c
  my_little_function(a, b, c)
  print("big: ", a, b, c)

def main():
  my_big_function(5, 2, 6)

main()


# Quiz 4, Feb 5, 2025
from cs1.graphics import *

def draw_thing(x, y):
    set_color('blue')
    draw_filled_polygon(x + 50, y, 
                        x + 30, y + 80, 
                        x, y + 100, 
                        x + 100, y + 100,
                        x + 70, y + 80)
    set_color('green')
    draw_filled_circle(x + 50, y + 80, 10)
    
def main():
    open_canvas(200, 200)
    draw_thing(0, 0)
    draw_thing(100, 0)
    draw_thing(0, 100)
    draw_thing(100, 100)
    
main()


# Quiz 5, Feb 10, 2025
## HINT: there are two erors:
### one "logical" error, preventing the program from doing "what I want" but otherwise invisible
### and one "semantic" error, causing the program to "throw an exception" (if the program ran)
## can you find both?
def tiny_helper_function_1(x, y):
  return 2 * x - y

def tiny_helper_function_2(x, y):
  return x * y + 1
  
def medium_helper_function(x, y):
  return tiny_helper_function_1(x, y) / tiny_helper_function_2(x, y)

def main():
  a = medium_helper_function(0, 0)
  c = medium_helper_function(1, 1)
  b = medium_helper_function(-1, 1)

# Quiz 6, Feb 14, 2025
def countdown(n):
  while n > 0:
    print(n, " ticks left!")
    n -= 1

def main():
  countdown(4)
  countdown(0)

main()

# Quiz 7, Feb 17, 2025
def main():
  count = 3
  while count <= 21:
      print(count)
      count = count + 3

main()

# Quiz 8, Feb 21, 2025
def helper1(x):
  if x < 12:
    return 10
  return 100

def helper2(y):
  result = 0
  while result < 9:
    result += y
  return result

def main():
  a = 14
  b = 4
  iterations = 0
  mystery = True
  while mystery:
    a -= 2
    b += 3
    iterations += 1
    mystery = helper1(a) > helper2(b)
  print(iterations)

main()

# Quiz 9, Mar 3, 2025
def get_valid_input():
  valid = False
  while not valid:
    response = input("Say a color!")
    if response == "red" or response == "green" or response == "blue":
      valid = True
  return response

def spell_color():
   color = get_valid_input()
   for letter in color: # this is new! can you guess what it does?
     print(letter, end = "!")

spell_color()

# Quiz 10, Mar 5, 2025
def magic_spell(n):
  for i in range(n):
    for j in range(i + 1):
     print('-', end='')
    print("X")

magic_spell(3)
magic_spell(4)

# Quiz 11, Mar 24, 2025
"my_data.txt"
'''
Hello class!
It is March 24.
I hope that we all learn something new!
'''
file = open("my_data.txt", "r")
for line in file:
  parts = line.split("a")
  print(line[3], line[5], line[7])
file.close()
file = open("my_data.txt", "w")
file.write("Goodbye!")
file.close()

# QuiZ 12, Mar 28, 2025
def encode(s):
  result = ""
  for i in range(len(s)):
    if s[i].isalpha():
      result += "."
    elif s[i].isdigit():
      result += "-"
    else:
      result += " "
  return result

encode("user!23")
encode("p4ss-w0rd")
encode("137 cats")

# Quiz 13, Mar 31, 2025
def decode(s):
  t = s[2:7]
  r = s[7::2]
  return t + r

print(decode("xyhappysjpirwimnlgt"))

# Quiz 14, Apr 2, 2025
def list_games(a, b):
  list_a = [7] * a
  list_b = [b, b, b]
  list_c = list_a + list_b
  list_c[a] = 'x'
  list_c[b] = 'y'
  return(list_c)

print(list_games(4, 2))