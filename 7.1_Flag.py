'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Flag is 494 px long
Stripes are 20 px tall
Union is 140px tall
Union is 197.6px long
Stars are 16.38px apart long way
Stars are 14.04px apart short way
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
'''
import arcade
arcade.open_window(494,260,"The Stars and Stripes")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

#stripes

for i in range(0,260,40):
    arcade.draw_lrtb_rectangle_filled(0,494,i+20,i,(191,10,48))

#blue union square

arcade.draw_lrtb_rectangle_filled(0,198,260,120,(0,40,104))

#stars

for h in range(120,260,28):
    for j in range(15,198,31):
        arcade.draw_text("*",j,h,arcade.color.WHITE,20)

for l in range(135,240,28):
    for k in range(30,170,31):
        arcade.draw_text("*",k,l,arcade.color.WHITE,20)

arcade.finish_render()

arcade.run()