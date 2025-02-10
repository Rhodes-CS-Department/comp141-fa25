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
