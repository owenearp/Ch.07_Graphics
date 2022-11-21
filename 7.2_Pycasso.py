'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade
arcade.open_window(500,700,"Owen Earp")
arcade.set_background_color((115,210,245))
arcade.start_render()

#street

arcade.draw_lrtb_rectangle_filled(0,500,125,0,(181,181,181))

for l in range(-50,550,60):
    arcade.draw_rectangle_filled(l,65,40,10,(255,255,255))

#curb and sidewalk

arcade.draw_lrtb_rectangle_outline(-5,505,145,126,(0,0,0))
arcade.draw_lrtb_rectangle_filled(0,500,144,127,(194,143,93))

arcade.draw_lrtb_rectangle_outline(-5,505,175,145,arcade.color.BLACK,2.5)
arcade.draw_lrtb_rectangle_filled(0,500,174,146,(222,186,150))

#gray background building

arcade.draw_lrtb_rectangle_outline(-5,60,525,176,(0,0,0,),1)
arcade.draw_lrtb_rectangle_filled(0,59,524,177,(191,201,214))

for a in range(3,60,40):
    arcade.draw_rectangle_outline(a,510,12,12,(0,0,0,))
for b in range(3,60,40):
    arcade.draw_rectangle_outline(b,480,12,12,(0,0,0,))

for a2 in range(3,60,40):
    arcade.draw_rectangle_filled(a2,510,11,11,(73,101,145))
for b2 in range(3,60,40):
    arcade.draw_rectangle_filled(b2,480,11,11,(73,101,145))

#tan background building

arcade.draw_lrtb_rectangle_outline(90,150,485,176,(0,0,0))
arcade.draw_lrtb_rectangle_filled(91,149,484,177,(217,205,218))

arcade.draw_rectangle_outline(105,470,12,12,(0,0,0))
arcade.draw_rectangle_filled(105,470,11,11,(73,101,145))

#yellow foreground building

arcade.draw_lrtb_rectangle_outline(-5,120,450,176,(0,0,0),2)
arcade.draw_lrtb_rectangle_filled(0,119,449,177,(243,195,110))

for c in range(275,450,65):
    arcade.draw_rectangle_outline(75,c,36,36,(0,0,0),2)
for c2 in range(275,450,65):
    arcade.draw_rectangle_filled(75,c2,35,35,(200,222,250))

for d in range(275,450,65):
    arcade.draw_rectangle_filled(75,d,36,4,(111,8,27))
for d2 in range(275,450,65):
    arcade.draw_rectangle_filled(75,d2,4,36,(111,8,27))

#yellow background building

arcade.draw_lrtb_rectangle_outline(270,330,485,176,(0,0,0))
arcade.draw_lrtb_rectangle_filled(275,329,484,177,(228,225,174))

for g in range(285,330,30):
    arcade.draw_rectangle_outline(g,470,12,12,(0,0,0))
for g2 in range(285,330,30):
    arcade.draw_rectangle_filled(g2,470,11,11,(67,77,130))

#blue foreground building

arcade.draw_lrtb_rectangle_outline(130,275,625,176,(0,0,0),2)
arcade.draw_lrtb_rectangle_filled(131,274,624,177,(101,204,201))

arcade.draw_lrtb_rectangle_outline(220,265,275,176,(0,0,0),2)
arcade.draw_lrtb_rectangle_filled(221,264,274,177,(63,141,141))
arcade.draw_line(242.5,176,242.5,275,(0,0,0),2)

for e in range(335,625,85):
    for e2 in range(160,275,85):
        arcade.draw_rectangle_outline(e2,e,25,25,(0,0,0),2)
arcade.draw_rectangle_outline(160,250,25,25,(0,0,0),2)

for f in range(335,625,85):
    for f2 in range(160,275,85):
        arcade.draw_rectangle_filled(f2,f,24,24,(195,232,241),2)
arcade.draw_rectangle_filled(160,250,24,24,(195,232,241),2)

#blue background building

arcade.draw_lrtb_rectangle_outline(345,405,535,176,(0,0,0))
arcade.draw_lrtb_rectangle_filled(346,404,534,177,(160,182,223))
for h in range(475,525,40):
    for h2 in range(355,405,20):
        arcade.draw_rectangle_outline(h2,h,12,12,(0,0,0))

for i in range(475,525,40):
    for i2 in range(355,405,20):
        arcade.draw_rectangle_filled(i2,i,11,11,(41,58,76))

#brown background building

arcade.draw_lrtb_rectangle_outline(440,505,475,176,(0,0,0))
arcade.draw_lrtb_rectangle_filled(441,500,474,177,(225,197,173))

#red foreground building

arcade.draw_lrtb_rectangle_outline(285,445,440,176,(0,0,0),2)
arcade.draw_lrtb_rectangle_filled(286,444,439,177,(220,104,89))

arcade.draw_lrtb_rectangle_outline(335,390,290,176,(0,0,0),2)
arcade.draw_lrtb_rectangle_filled(336,389,289,177,(132,69,60))
arcade.draw_line(362.5,176,362.5,290,(0,0,0),2)

arcade.draw_lrtb_rectangle_outline(280,450,455,440,(0,0,0),2)
arcade.draw_lrtb_rectangle_filled(281,449,454,441,(185,163,149))

for j in range(315,445,100):
    arcade.draw_rectangle_outline(j,390,35,55,(0,0,0),2)
    arcade.draw_rectangle_filled(j,390,34,54,(195,228,255))

arcade.draw_line(297.5,390,332.5,390,(0,0,0),2.5)
arcade.draw_line(397.5,390,432.5,390,(0,0,0),2.5)
arcade.draw_line(315,362.5,315,417.5,(0,0,0),2.5)
arcade.draw_line(415,362.5,415,417.5,(0,0,0),2.5)

#pink foreground building

arcade.draw_lrtb_rectangle_outline(455,505,545,176,(0,0,0),2)
arcade.draw_lrtb_rectangle_filled(456,500,544,177,(205,153,176))

for k in range(342,545,80):
    arcade.draw_rectangle_outline(480,k,25,33,(0,0,0),2)
    arcade.draw_rectangle_filled(480,k,24,32,(202,225,255))
    arcade.draw_rectangle_filled(480,k,2.5,33,(111,8,27))

#sun

arcade.draw_circle_filled(500,700,75,(255,255,0))
arcade.draw_circle_outline(500,700,76,(0,0,0))

arcade.finish_render()


arcade.run()



