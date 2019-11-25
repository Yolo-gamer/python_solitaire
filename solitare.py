import turtle,os,time,math
from random import randint,sample,randrange
from PIL import Image,ImageTk
screen = turtle.Screen()
imgs =['CARDS\\AC.gif', 'CARDS\\AD.gif', 'CARDS\\AH.gif', 'CARDS\\AS.gif', 'CARDS\\2C.gif', 'CARDS\\2D.gif', 'CARDS\\2H.gif', 'CARDS\\2S.gif', 'CARDS\\3C.gif', 'CARDS\\3D.gif', 'CARDS\\3H.gif', 'CARDS\\3S.gif', 'CARDS\\4C.gif', 'CARDS\\4D.gif', 'CARDS\\4H.gif', 'CARDS\\4S.gif', 'CARDS\\5C.gif', 'CARDS\\5D.gif', 'CARDS\\5H.gif', 'CARDS\\5S.gif', 'CARDS\\6C.gif', 'CARDS\\6D.gif', 'CARDS\\6H.gif', 'CARDS\\6S.gif', 'CARDS\\7C.gif', 'CARDS\\7D.gif', 'CARDS\\7H.gif', 'CARDS\\7S.gif', 'CARDS\\8C.gif', 'CARDS\\8D.gif', 'CARDS\\8H.gif', 'CARDS\\8S.gif', 'CARDS\\9C.gif', 'CARDS\\9D.gif', 'CARDS\\9H.gif', 'CARDS\\9S.gif', 'CARDS\\10C.gif', 'CARDS\\10D.gif', 'CARDS\\10H.gif', 'CARDS\\10S.gif', 'CARDS\\JC.gif', 'CARDS\\JD.gif', 'CARDS\\JH.gif', 'CARDS\\JS.gif', 'CARDS\\QC.gif', 'CARDS\\QD.gif', 'CARDS\\QH.gif', 'CARDS\\QS.gif', 'CARDS\\KC.gif', 'CARDS\\KD.gif', 'CARDS\\KH.gif', 'CARDS\\KS.gif']
imgs.reverse()

col1_down_back=[]#0
col1_down=[]#0 
col1_up=[]#1
col1_location=(-300, 100)

col2_down_back=[]#1
col2_down=[]#1 
col2_up=[]#1
col2_location=(-200, 100)

col3_down_back=[]#2
col3_down=[]#2 
col3_up=[]#1
col3_location=(-100, 100)

col4_down_back=[]#3
col4_down=[]#3
col4_up=[]#1
col4_location=(0, 100)

col5_down_back=[]#4
col5_down=[]#4 
col5_up=[]#1
col5_location=(100, 100)

col6_down_back=[]#5
col6_down=[]#5
col6_up=[]#1
col6_location=(200, 100)

col7_down_back=[]#6
col7_down=[]#6 
col7_up=[]#1
col7_location=(300, 100)

dum1=[]
dum2=[]
dum3=[]
dum4=[]
dum_pos=[0,0,0,0]
dum1_location=(100, 250)
dum2_location=(200, 250)
dum3_location=(300, 250)
dum4_location=(400, 250)

draw_pile=[]#24 
draw1=[]#0 
draw2=[]#0 
draw3=[]#0 
draw_pile_location=(-400, 250)
draw1_location=(-300, 250)
draw2_location=(-200, 250)
draw3_location=(-100, 250)

screen.bgcolor("lightblue")

cards=[]
leng=len(imgs)-1
screen.bgcolor("lightblue")

card_blank=turtle.Turtle()
card_blank.ht()
card_percent=turtle.Turtle()
card_percent.ht()
card_percent.pu()
card_percent.sety(card_percent.ycor()+150)
card_percent.setx(card_percent.xcor()-25)

def add_cards():
    return cards.pop(randrange(len(cards)))
  
def add_backs():
    return card_backs.pop(0)
  
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
  
card_backs=[]
purple_backs=[]
deck_back=[]

def make_backs():
    rand="CARDS\\red_back.gif"
    name=os.path.basename(rand).split(".")[0]
    screen.addshape(rand)
    card_percent.write("loading cards")
    for n in range(52):
        card_percent.clear()
        card_percent.write("cards loaded "+str(n)+"/52")
        card=card_blank.clone()
        card.goto(0,0)
        card.shape(rand)
        card.pu()
        #card.st()
        card.speed(1000000)
        card_backs.append(card)
    card=card_blank.clone()
    card.goto(0,0)
    card.shape(rand)
    card.pu()
    #card.st()
    card.speed(1000000)
    deck_back.append(card)
    card_percent.clear()
def purple_back():
    rand="CARDS\\purple_back.gif"
    name=os.path.basename(rand).split(".")[0]
    screen.addshape(rand)
    card=card_blank.clone()
    card.goto(0,0)
    card.shape(rand)
    card.pu()
    #card.st()
    card.speed(1000000)
    purple_backs.append(card)
def make_cards():
    card_percent.write("loading cards")
    time.sleep(1)
    for i,n in enumerate(imgs):
        card_percent.clear()
        card_percent.write("cards loaded "+str(i)+"/"+str(len(imgs)))
        rand=n
        name=os.path.basename(rand).split(".")[0]
        screen.addshape(rand)
        card=card_blank.clone()
        card.goto(0,0)
        card.shape(rand)
        card.dragging=False
        card.pu()
        types=[name[:-1],name[-1]]
        card.suit=types[1]
        card.value=types[0]
        #card.st()
        card.speed(1000000)
        cards.append(card)
    card_percent.clear()
    
def fill():
    col1_up.append(add_cards())
    col2_up.append(add_cards())
    col3_up.append(add_cards())
    col4_up.append(add_cards())
    col5_up.append(add_cards())
    col6_up.append(add_cards())
    col7_up.append(add_cards())
    col2_down.append(add_cards())
    for n in range(2):
        col3_down.append(add_cards())
    for n in range(3):
        col4_down.append(add_cards())
    for n in range(4):
        col5_down.append(add_cards())
    for n in range(5):
        col6_down.append(add_cards())
    for n in range(6):
        col7_down.append(add_cards())
    col2_down_back.append(add_backs())
    for n in range(2):
        col3_down_back.append(add_backs())
    for n in range(3):
        col4_down_back.append(add_backs())
    for n in range(4):
        col5_down_back.append(add_backs())
    for n in range(5):
        col6_down_back.append(add_backs())
    for n in range(6):
        col7_down_back.append(add_backs())
    for n in range(24):
        draw_pile.append(add_cards())
        
def cards_mover(cols_up,cols_down,cols_card_backs,location):
    for i,n in enumerate(cols_down+cols_up):
        n.goto(location[0],location[1]-i*20)
        n.org_x=location[0]
        n.org_y=location[1]-i*20
        if n in cols_up:
            n.st()
        else:
            cols_card_backs[i].goto(location[0],location[1]-i*20)
            cols_card_backs[i].st()
            
def draw_pile_mover(draw,location):
    for i,n in enumerate(draw):
        n.goto(location[0]+100,location[1])
        n.org_x=location[0]+100
        n.org_y=location[1]
        
def move_cards():
    cards_mover(col1_up,col1_down,col1_down_back,col1_location)
    cards_mover(col2_up,col2_down,col2_down_back,col2_location)
    cards_mover(col3_up,col3_down,col3_down_back,col3_location)
    cards_mover(col4_up,col4_down,col4_down_back,col4_location)
    cards_mover(col5_up,col5_down,col5_down_back,col5_location)
    cards_mover(col6_up,col6_down,col6_down_back,col6_location)
    cards_mover(col7_up,col7_down,col7_down_back,col7_location)
    draw_pile_mover(draw_pile,draw_pile_location)
def type_test(new_card_suit,new_card_value,current_card_suit,current_card_value):
    list_test=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    if list_test.index(new_card_value)-1 == list_test.index(current_card_value):
      if current_card_suit in ["H","D"] and new_card_suit in ["S","C"] or current_card_suit in ["S","C"] and new_card_suit in ["H","D"]:
        return True
      else:
        return False
    else:
      return False
def type_test2(new_card_suit,new_card_value,current_card_suit,current_card_value):
    list_test=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    if list_test.index(new_card_value)+1 == list_test.index(current_card_value):
      if current_card_suit == new_card_suit:
        return True
      else:
        return False
    else:
      return False
def flip(column):
    column=column.split("_")[0]
    down_pile=eval(str(column)+"_down")
    up_pile=eval(str(column)+"_up")
    if len(down_pile) > 0 and len(up_pile) == 0:
        exec(str(column)+"_down_back[-1].ht()")
        exec(str(column)+"_down_back.pop(-1)")
        exec(str(column)+"_down[-1].st()")
        exec(str(column)+"_up.append("+str(column)+"_down.pop(-1))")
def dum_cards(card_column):
    dum_pos[int(card_column[-1])-1]-=1
    if eval("len("+card_column+")") > 0:
        exec(card_column+"[-1].st()")
def show_prev_draw():
    global pos
    pos-=1
    try:
        draw_pile[pos-1].st()
    except:
        pos+=1
def place_card(x, y,card,val):
    if len(col1_up) > 0 :col1_up_top=col1_up[-1]
    else: col1_up_top=col1_location

    if len(col2_up) > 0 :col2_up_top=col2_up[-1]
    else: col2_up_top=col2_location

    if len(col3_up) > 0 :col3_up_top=col3_up[-1]
    else: col3_up_top=col3_location

    if len(col4_up) > 0 :col4_up_top=col4_up[-1]
    else: col4_up_top=col4_location

    if len(col5_up) > 0 :col5_up_top=col5_up[-1]
    else: col5_up_top=col5_location

    if len(col6_up) > 0 :col6_up_top=col6_up[-1]
    else: col6_up_top=col6_location

    if len(col7_up) > 0 :col7_up_top=col7_up[-1]
    else: col7_up_top=col7_location

    if len(dum1) > 0 :dum1_up_top=dum1[-1]
    else: dum1_up_top=dum1_location

    if len(dum2) > 0 :dum2_up_top=dum2[-1]
    else: dum2_up_top=dum2_location

    if len(dum3) > 0 :dum3_up_top=dum3[-1]
    else: dum3_up_top=dum3_location

    if len(dum4) > 0 :dum4_up_top=dum4[-1]
    else: dum4_up_top=dum4_location
    
    card_column=None

    if card in col1_up:card_column="col1_up"
    if card in col2_up:card_column="col2_up"
    if card in col3_up:card_column="col3_up"
    if card in col4_up:card_column="col4_up"
    if card in col5_up:card_column="col5_up"
    if card in col6_up:card_column="col6_up"
    if card in col7_up:card_column="col7_up"
    if card in draw_pile:card_column="draw_pile"
    if card in dum1:card_column="dum1"
    if card in dum2:card_column="dum2"
    if card in dum3:card_column="dum3"
    if card in dum4:card_column="dum4"
    new_distance=10000000000000
    next_card=None
    column=0
    dum=0
    for n in range(7):
      if eval("col"+str(n+1)+"_up_top") != card :
          try:
            distance=dist((x,y),eval("col"+str(n+1)+"_up_top.pos()"))
          except:
            distance=dist((x,y),eval("col"+str(n+1)+"_up_top"))
          if distance < new_distance:
            new_distance=distance
            next_card=eval("col"+str(n+1)+"_up_top")
            column=n+1
    for n in range(4):
      if eval("dum"+str(n+1)+"_up_top") != card :
          try:
            distance=dist((x,y),eval("dum"+str(n+1)+"_up_top.pos()"))
          except:
            distance=dist((x,y),eval("dum"+str(n+1)+"_up_top"))
          if distance < new_distance:
            new_distance=distance
            next_card=eval("dum"+str(n+1)+"_up_top")
            dum=n+1
            column=0
    if column == 0 and not "dum" in card_column and val == True:
        if type(next_card) == tuple:
            if card.value == "A":
              eval("dum"+str(dum)+".append("+card_column+".pop("+card_column+".index(card)))")
              card.org_x,card.org_y=next_card[0],next_card[1]
              if card_column != "draw_pile":
                  flip(card_column)
              else:
                  show_prev_draw()
        elif type_test2(next_card.suit,next_card.value,card.suit,card.value) == True:
          exec("dum"+str(dum)+".append("+card_column+".pop("+card_column+".index(card)))")
          exec("dum"+str(dum)+"[dum_pos["+str(dum-1)+"]].ht()")
          dum_pos[dum-1]+=1
          card.org_x,card.org_y=next_card.pos()[0],next_card.pos()[1]
          if card_column != "draw_pile":
              flip(card_column)
          else:
              show_prev_draw()
    elif column != 0:
        if type(next_card) == tuple:
          eval("col"+str(column)+"_up.append("+card_column+".pop("+card_column+".index(card)))")
          card.org_x,card.org_y=next_card[0],next_card[1]
          val=True
          if card_column != "draw_pile" and not "dum" in card_column:
              flip(card_column)
          elif not "dum" in card_column:
              show_prev_draw()
          else:
              dum_cards(card_column)
        elif type_test(next_card.suit,next_card.value,card.suit,card.value) == True:
          eval("col"+str(column)+"_up.append("+card_column+".pop("+card_column+".index(card)))")
          card.org_x,card.org_y=next_card.pos()[0],next_card.pos()[1]-20
          val=True
          if card_column != "draw_pile" and not "dum" in card_column:
              flip(card_column)
          elif not "dum" in card_column:
              show_prev_draw()
          else:
              dum_cards(card_column)
    
    card.goto(card.org_x,card.org_y)
    return val
purple_back()
tables=purple_backs[-1]
tables.org_x,tables.org_y=tables.pos()
tables.goto(dum1_location)
tables.stamp()
tables.goto(dum2_location)
tables.stamp()
tables.goto(dum3_location)
tables.stamp()
tables.goto(dum4_location)
tables.stamp()
tables.goto(col1_location)
tables.stamp()
tables.goto(col2_location)
tables.stamp()
tables.goto(col3_location)
tables.stamp()
tables.goto(col4_location)
tables.stamp()
tables.goto(col5_location)
tables.stamp()
tables.goto(col6_location)
tables.stamp()
tables.goto(col7_location)
tables.stamp()
tables.goto(tables.org_x,tables.org_y)

make_backs()
make_cards()
def release(x,y,card):
    card_column=None
    if card in col1_up:card_column="col1_up"
    if card in col2_up:card_column="col2_up"
    if card in col3_up:card_column="col3_up"
    if card in col4_up:card_column="col4_up"
    if card in col5_up:card_column="col5_up"
    if card in col6_up:card_column="col6_up"
    if card in col7_up:card_column="col7_up"
    if card in draw_pile:card_column="draw_pile"
    if card in dum1:card_column="dum1"
    if card in dum2:card_column="dum2"
    if card in dum3:card_column="dum3"
    if card in dum4:card_column="dum4"
    stack_len=eval("len("+card_column+")")
    stack_pos=eval(card_column+".index(card)")
    if stack_len-stack_pos <= 1 or card_column=="draw_pile" :
        place_card(x,y,card,True)
    else:
        if place_card(x,y,card,False) == True:
            cards=eval(card_column+"[stack_pos:]")
            for i,n in enumerate(cards):
                place_card(x,y-(20*i),n,False)
    try:
        if dum1[-1].value=="K" and dum2[-1].value=="K" and dum3[-1].value=="K" and dum4[-1].value=="K":
            print("congrads")
    except:
        pass
for numb in range(len(cards)):
    cards[numb].ondrag(cards[numb].goto)
    #exec("cards[numb].onclick(lambda x, y,card=cards["+str(numb)+"]: dum_cards(x, y,card))")
    #exec("cards[numb].onrelease(lambda x, y,card=cards["+str(numb)+"]: place_card(x, y,card))")
    exec("cards[numb].onrelease(lambda x, y,card=cards["+str(numb)+"]: release(x, y,card))")

fill()
move_cards()

pos=0

def next_card(x,y):
    global pos
    if len(draw_pile)-1 < pos:
        pos=0
    draw_pile[pos-1].ht()
    draw_pile[pos].st()
    pos+=1


deck_back[0].onclick(next_card)
deck_back[0].goto(draw_pile_location)
deck_back[0].st()

