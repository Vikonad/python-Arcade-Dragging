import arcade

class Windows:
    def __init__(self,x,y,title,color):
        self.x, self.y, self.title, self.color = x, y, title, color

    def add_window(self):
        arcade.draw_rectangle_filled(self.x,self.y,100,100,self.color)

class DrawingApp(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(title="Dragging",width=880,height=587)
        self.allwindows = [
            Windows(100,100,"",arcade.color.RED),
            Windows(200,100,"",arcade.color.GREEN),
            Windows(300,100,"",arcade.color.CYAN),
            Windows(400,100,"",arcade.color.PURPLE),
            Windows(500,100,"",arcade.color.PINK),
            Windows(600,100,"",arcade.color.WHITE)
        ]
        self.drag = [False,self.allwindows[-1]]
    
    def on_mouse_press(self, x, y, button, modifiers):
        for i in self.allwindows[::-1]:
            if (i.x-50 < x < i.x+50) and i.y-50 < y < i.y+50:
                self.drag[1] = i
                self.allwindows.remove(i)
                self.allwindows.append(i)
                self.drag[0] = True
                break
    
    def on_mouse_release(self, x, y, button, modifiers):
        self.drag[0] = False

    def on_draw(self):
        arcade.start_render()
        if self.drag[0]:
            self.drag[1].x = self._mouse_x
            self.drag[1].y = self._mouse_y
        for i in self.allwindows:
            i.add_window()
        #arcade.draw_rectangle_filled(self.xx,self.yy,20,20,arcade.color.GREEN)

def main():
    window = DrawingApp(800, 600, "Drawing App")
    arcade.run()

if __name__ == "__main__":
    main()
