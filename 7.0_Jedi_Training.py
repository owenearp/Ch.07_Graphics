#Sign your name:_Owen Earp__________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500,400,"Jedi Training")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()

# grid stuff

for i in range(0,500,20):
    arcade.draw_line(0,i,500,i,arcade.color.BLACK,1)

for j in range(0,500,20):
    arcade.draw_line(j,0,j,500,arcade.color.BLACK,1)

#pink box top left

arcade.draw_lrtb_rectangle_filled(20,80,380,360,arcade.color.PHLOX)

#red point bottom right

arcade.draw_circle_filled(460,10,4,arcade.color.RED)

#blue line bottom left

arcade.draw_line(80,20,120,60,arcade.color.BLUE,1)

#yellow ellipse

arcade.draw_ellipse_filled(100,100,120,40,arcade.color.AMBER)

#purple circle

arcade.draw_circle_filled(250,200,40,arcade.color.WISTERIA)

#pink words

arcade.draw_text("I love you. I know.",20,160,arcade.color.BLUSH,20)

#pink box middle

arcade.draw_rectangle_filled(200,260,40,20,arcade.color.BLUSH,-45)

#pacman

arcade.draw_arc_filled(400,320,120,120,arcade.color.YELLOW,30,330)

arcade.finish_render()

arcade.run()