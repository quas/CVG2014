#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import math

def getSidesQuadrangle(quadrangle):
    '''function returning dict with all sides from quadrangle and diagonal
     sample: {'bottom': 18.33617570306381, 'diagonal_right_top_to_bottom': 22.808803673745274,
              'right': 12.389373592397579, 'top': 15.542883805607614, 'left': 10.099416775868294,
              'diagonal_left_bottom_to_top': 17.396951686816895}'''

    #Pythagoras: sqrt((x1-x2)**2 +(y1-y2)**2 +(z1-z2)**2) get vector

    left_side = math.sqrt((quadrangle[0][0][0]-quadrangle[1][0][0])**2 + # left side
                          (quadrangle[0][0][1]-quadrangle[1][0][1])**2 +
                          (quadrangle[0][1] - quadrangle[1][1]))
    right_side = math.sqrt((quadrangle[2][0][0]-quadrangle[3][0][0])**2 + # right side
                          (quadrangle[2][0][1]-quadrangle[3][0][1])**2 +
                          (quadrangle[2][1] - quadrangle[3][1]))
    top_side = math.sqrt((quadrangle[1][0][0]-quadrangle[3][0][0])**2 + # top side
                          (quadrangle[1][0][1]-quadrangle[3][0][1])**2 +
                          (quadrangle[1][1] - quadrangle[3][1]))
    bottom_side = math.sqrt((quadrangle[0][0][0]-quadrangle[2][0][0])**2 + # bottom side
                          (quadrangle[0][0][1]-quadrangle[2][0][1])**2 +
                          (quadrangle[0][1] - quadrangle[2][1]))

    diagonal1 = quadrangle[0], quadrangle[3]

    # Pythagoras: sqrt((x1-x2)**2 +(y1-y2)**2 +(z1-z2)**2)
    diagonal_left_bottom_to_top = math.sqrt((diagonal1[0][0][0]-diagonal1[1][0][0])**2 + #диагональ от нижней левой точки к
                          (diagonal1[0][0][1]-diagonal1[1][0][1])**2 + #верхней правой
                          (diagonal1[0][1]-diagonal1[1][1]))

    sides = {'left':left_side,'right':right_side,
             'top':top_side,'bottom':bottom_side,
             'diagonal_left_bottom_to_top':diagonal_left_bottom_to_top}

    # 'diagonal_right_top_to_bottom':diagonal_left_top_to_bottom

    return sides

def getTriangles(Quadrangle_sides):
    # function returning two triangles
    top_triangle = Quadrangle_sides['left'], \
                   Quadrangle_sides['top'], \
                   Quadrangle_sides['diagonal_left_bottom_to_top']
    bottom_triangle = Quadrangle_sides['right'], \
                      Quadrangle_sides['bottom'], \
                      Quadrangle_sides['diagonal_left_bottom_to_top']

    return top_triangle, bottom_triangle

def getAnglesTriangle(triangle):
    ''' function get triangle (3 side_sizes)
    and returning the 3 angles of triangle'''

    #Pythagoras: arccos((a**2+b**2-c**2)/(2ab)) get angle
    side1 = triangle[0]
    side2 = triangle[1]
    side3 = triangle[2]
    Angle1 = round(math.degrees(math.acos((side1**2 + side2**2 - side3**2) # radians to angle and round to 4 digits
                                        /(2*side1*side2))), 4)
    Angle2 = round(math.degrees(math.acos((side1**2 + side3**2 - side2**2)
                                        /(2*side1*side3))), 4)
    Angle3 = round(math.degrees(math.acos((side2**2 + side3**2 - side1**2)
                                        /(2*side2*side3))), 4)
    return Angle1, Angle2, Angle3

def getTypeQuadrangle(quadrangle):
    ''' function returning quadrangle type
        foursquare, rectangle, or just quadrangle'''

    Quadrangle_sides = getSidesQuadrangle(quadrangle)
    # Quadrangle_sides its a dict: {'left': 10.099416775868294, 'diagonal_right_top_to_bottom': 22.808803673745274,
    # 'top': 15.542883805607614, 'bottom': 18.33617570306381,
    # 'right': 12.389373592397579, 'diagonal_left_bottom_to_top': 17.396951686816895}

    if Quadrangle_sides['left'] == Quadrangle_sides['right'] and \
       Quadrangle_sides['left'] == Quadrangle_sides['top'] and \
       Quadrangle_sides['left'] == Quadrangle_sides['bottom']:
        quadrangle_type = 'foursquare'
        return quadrangle_type

    if Quadrangle_sides['left'] == Quadrangle_sides['right'] and \
         Quadrangle_sides['top'] == Quadrangle_sides['bottom']:
        Triangles = getTriangles(Quadrangle_sides)
        Top_triangle = Triangles[0]
        Bottom_triangle = Triangles[1]
        Angle1, Angle2, Angle3 = getAnglesTriangle(Top_triangle)
        Angle11, Angle22, Angle33 = getAnglesTriangle(Bottom_triangle)
        if Angle1 == 90 or Angle2 == 90 or Angle3 == 90 and \
           Angle11== 90 or Angle22== 90 or Angle33== 90:
            quadrangle_type = 'rectangle'
            return quadrangle_type
    else:
        quadrangle_type = 'quadrangle' #Heron
        return quadrangle_type

def getVolumeQuadrangle(quadrangle, quadrangle_type, static_height):
    # function returned volume quadrangle
    Quadrangle_sides = getSidesQuadrangle(quadrangle)
    quadrangle = sorted(quadrangle, key=lambda point: abs(point[1]))
    height = quadrangle[-1][1] # get a biggest height
    difference_height = height - static_height \
                        if height < static_height \
                        else static_height - height
    if quadrangle_type is 'foursquare': #Pythagoras
        V = Quadrangle_sides['left'] ** 3
        return V
    elif quadrangle_type is 'rectangle': #Pythagoras
        V = Quadrangle_sides['left']*Quadrangle_sides['bottom']*height
        return V
    else: #Heron
        top_triangle, bottom_triangle = getTriangles(Quadrangle_sides)
        s1 = (top_triangle[0] + top_triangle[1] + top_triangle[2])/2 # semi perimeter Heron's formula
        s2 = (bottom_triangle[0] + bottom_triangle[1] + bottom_triangle[2])/2
        S1 = math.sqrt(s1*(s1-top_triangle[0])*(s1-top_triangle[1])*(s1 - top_triangle[2]))
        S2 = math.sqrt(s2*(s2-bottom_triangle[0])*(s2-bottom_triangle[1])*(s2 - bottom_triangle[2]))
        V = (S1+S2)*abs(difference_height)
        return V


