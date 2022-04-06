import turtle
t = turtle.Turtle()
zelE = int(input("tedad azlaE ra vared konid: "))
tol = int(input("tol har zelE ra vared konid : "))

for i in range(zelE):
    for j in range(zelE):
	    turtle.forward(tol)
    	turtle.right(360 / zelE)
        zelE = zelE + 1
        tol = tol + 1


