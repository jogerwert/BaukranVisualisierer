from vpython import *

def generate_Baufeld(parameter_input_x, parameter_input_y):
    L = W = 1
    H = 0.1
    for x in range(0, parameter_input_x):
        for y in range(0, parameter_input_y):
            if not x % 2 == 0:
                if y % 2 == 0:
                    color_Baufeld = vector(1, 0, 0)
                else:
                    color_Baufeld = vector(0, 0, 1)
            else:
                if y % 2 == 1:
                    color_Baufeld = vector(1, 0, 0)
                else:
                    color_Baufeld = vector(0, 0, 1)

            box(pos=vector(x, 0, y), length=L, height=H, width=W, color=color_Baufeld)


def generate_Kran(parameter_input_hoehe):
    L = W = H = 1
    cylinder(pos=vector(5, 0, 0), radius=0.5, length=parameter_input_hoehe, axis=vector(0, 1, 0))
    cylinder(pos=vector(5, parameter_input_hoehe, 0), radius=0.5, length=parameter_input_hoehe, axis=vector(0, 0, 1))
    box(pos=vector(5, parameter_input_hoehe - 1, 1), length=L, height=H, width=W, color=vector(0, 1, 0))


def generate_Hindernis(parameter_input_hoehe):
    #cone(pos=vector(5, 0, 2), radius=0.5, axis= vector(0, parameter_input_hoehe, 0), color=vector(1, 0, 1))
    box(pos=vector(5, 0, 2), color=vector(1, 0, 1))

def generate_Bauteil():
    box(pos=vector(5, 0, 5), color=vector(0, 0, 0))

generate_Baufeld(10, 7)
generate_Kran(10)
generate_Hindernis(8)
generate_Bauteil()