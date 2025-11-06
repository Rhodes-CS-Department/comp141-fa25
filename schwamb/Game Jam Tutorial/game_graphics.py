# Holds all the functions to play a computerized version of Up & Down the River
import ipywidgets as widgets
import IPython.display as disp
from cs1.graphics import *

##### show_title() #####
# show_title shows the title screen
def show_title():
    open_canvas(550,250)
    draw_string('Up & Down the River',250,50,30)
    draw_river()
    draw_boat()

def draw_river():
    set_color_rgb(0,187,255)
    draw_filled_polygon(50,100,100,125,150,100,200,125,250,100,300,125,350,100,400,125,450,100,
                        450,150,400,175,350,150,300,175,250,150,200,175,150,150,100,175,50,150)

def draw_boat():
    set_color('brown')
    draw_filled_oval(100,113,20,13)
    set_color('black')
    set_line_thickness(2)
    draw_oval(100,113,20,13)
    draw_oval(100,110,20,10)
    set_line_thickness(5)
    draw_line(100, 105, 95, 135)
    set_line_thickness(8)
    draw_line(95,133,93,140)

def show_trump(trump_suit):
    clear_canvas()
    set_color('black')
    draw_string('Trump Suit: '+trump_suit,250,50,30)
    draw_card(200,75,'  of '+trump_suit)
    input('Trump Suit: '+trump_suit+' (press enter to continue)')

def show_cards(hands,player_name):
    clear_canvas()
    set_color('black')
    draw_string('Showing '+player_name+'\'s Hand',250,50,30)
    draw_string('Press Enter to View',250,100,30)
    input("")
    x = 5
    y = 75
    x_offset = 490//(len(hands[player_name])+1)
    clear_canvas()
    draw_string(player_name+'\'s Hand',250,50,30)
    for card in hands[player_name]:
        draw_card(x,y,card)
        x += x_offset

def show_final_cards(cards_to_show,player_name):
    clear_canvas()
    set_color('black')
    draw_string('Showing Cards '+player_name+' Can See',250,50,30)
    draw_string('Press Enter to View',250,100,30)
    input("")
    x = 5
    y = 75
    x_offset = 490//(len(cards_to_show)+1)
    clear_canvas()
    draw_string('Cards '+player_name+' Can See',250,50,30)
    for card in cards_to_show:
        draw_card(x,y,card)
        x += x_offset

def show_bids(n_bids,n_cards):
    clear_canvas()
    set_color('black')
    draw_string(str(n_bids)+' tricks have been bid for.',250,50,30)
    draw_string('There are '+str(n_cards)+' total tricks.',250,100,30)
    draw_string('Press Enter to continue.',250,150,30)
    input("")

def show_trick(played_cards):
    clear_canvas()
    set_color('black')
    draw_string('Cards Played - Press Enter to Continue',250,50,25)
    x = 10
    y = 75
    x_offset = 480/(len(played_cards)+1)
    for card in played_cards:
        draw_card(x,y,card)
        x += x_offset
    input("")

def show_tricks_won(tricks):
    clear_canvas()
    set_color('black')
    draw_string('Tricks Won - Press Enter to Continue',250,50,25)
    x = 250
    y = 75
    for player in tricks.keys():
        draw_string(player+': '+str(tricks[player]),x,y,20)
        y += 20
    input("")

def show_score(score):
    clear_canvas()
    set_color('black')
    draw_string('Score - Press Enter to Continue',250,50,25)
    x = 250
    y = 75
    for player in score.keys():
        draw_string(player+': '+str(score[player]),x,y,20)
        y += 20
    input("")

def draw_card(x,y,card_name):
    set_color('white')
    draw_filled_rect(x,y,100,150)
    set_color('black')
    set_line_thickness(2)
    draw_rect(x,y,100,150)
    card_char, card_suit = card_name.split(' of ')
    if len(card_char) > 2:
        card_char = card_char[0]
    if card_suit == 'Diamonds':
        # top diamond & value
        draw_diamond(x+10, y+20, 10, 20)
        draw_string(card_char, x+25, y+25, 20)
        # bottom diamond and value
        draw_diamond(x+90, y+130, 10, 20)
        draw_string(card_char, x+75, y+135, 20)
        # center diamond
        draw_diamond(x+50, y+75, 50, 75)
    elif card_suit == 'Clubs':
        # top club and value
        draw_club(x+10, y+20, 10, 20)
        draw_string(card_char, x+25, y+25, 20)
        # bottom club and value
        draw_club(x+90, y+130, 10, 20)
        draw_string(card_char, x+75, y+135, 20)
        # center club
        draw_club(x+50, y+75, 50, 75)
    elif card_suit == 'Hearts':
        # top heart and value
        draw_heart(x+10, y+20, 10, 20)
        draw_string(card_char, x+25, y+25, 20)
        # bottom heart and value
        draw_heart(x+90, y+130, 10, 20)
        draw_string(card_char, x+75, y+135, 20)
        # center heart
        draw_heart(x+50, y+75, 50, 75)
    else:
        # top spade and value
        draw_spade(x+10, y+20, 10, 20)
        draw_string(card_char, x+25, y+25, 20)
        # bottom spade and value
        draw_spade(x+90, y+130, 10, 20)
        draw_string(card_char, x+75, y+135, 20)
        # center spade
        draw_spade(x+50, y+75, 50, 75)

def draw_diamond(x, y, w, h):
    set_color('red')
    draw_filled_polygon(x-w/2,y, x,y+h/2, x+w/2,y, x,y-h/2)

def draw_club(x, y, w, h):
    set_color('black')
    r = w/4
    draw_filled_circle(x-r,y-r/4,r)
    draw_filled_circle(x+r,y-r/4,r)
    draw_filled_circle(x,y-h/4,r)
    draw_filled_polygon(x,y, x-r,y+h/4, x+r,y+h/4)

def draw_heart(x, y, w, h):
    set_color('red')
    r = w/4
    draw_filled_circle(x-r,y-h/3,r)
    draw_filled_circle(x+r,y-h/3,r)
    draw_filled_polygon(x-0.515*w,y-h/3, x,y+h/3, x+0.515*w,y-h/3)

def draw_spade(x, y, w, h):
    set_color('black')
    r = w/4
    draw_filled_circle(x-r,y,r)
    draw_filled_circle(x+r,y,r)
    draw_filled_polygon(x-0.525*w,y, x,y-h/2, x+0.525*w,y)
    draw_filled_polygon(x,y, x-r,y+h/4, x+r,y+h/4)

def clear_text_output():
    _canvas = get_canvas()
    disp.clear_output(wait=False)
    _out = widgets.AppLayout(center=_canvas)
    disp.display(_out)