import arcade
arcade.open_window(600,600,"My Drawing")
arcade.set_background_color(arcade.color.ANDROID_GREEN)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0,200,200,0,(255,0,0))
arcade.draw_rectangle_filled(300,300,400,400,(0,255,0,100),45)
arcade.draw_rectangle_outline(300,300,400,400,(0,0,0),3,45)
arcade.draw_point(300,300,(0,0,0,),3)
arcade.draw_line(100,100,500,500,(255,255,0),4)
arcade.draw_circle_filled(300,300,50,(255,255,255,200))
arcade.draw_circle_outline(300,300,50,(0,0,0),3)
arcade.draw_ellipse_filled(400,400,100,50,(255,255,0))
point_list=((100,100),(120,400),(200,400),(300,150))
arcade.draw_polygon_filled(point_list,arcade.color.ALIZARIN_CRIMSON)
arcade.draw_text("Ay yuh",200,550,arcade.color.BISTRE,20)
# pic = arcade.load_texture("python.png")
# arcade.draw_texture_rectangle(550,100,pic.width,pic.height,pic,45)
for x in range(0,610,20):
    arcade.draw_rectangle_filled(x,60,10,30,arcade.color.WHITE)

arcade.draw_rectangle_filled(300,67,600,5,arcade.color.WHITE)
arcade.draw_rectangle_filled(300,52,600,5,arcade.color.WHITE)

radius = 50
y = 50
for i in range(3):
    arcade.draw_circle_filled(100,y,radius,(255,255,243))
    y = y+1.8*radius
    radius = radius * 0.8
arcade.finish_render()











arcade.run()