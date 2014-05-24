#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from xml.etree import ElementTree as ET

def getPointsFromXmlFile(xml_file): #OK!
    """ function after parse file.xml returns an array of points of the form:
        [[(y1,x1)z1],[(y2,x2)z2]...[...n]] where z is a height """

    points = []
    cache = []
    with open(xml_file, 'r', encoding='utf-8') as file:
        tree = ET.parse(file)
    ROOT = tree.getroot()
    CgPoints = ROOT[-1]
    for point in CgPoints:
        cache.append(point.text)
    for str_point in cache:
        str_point = list(str_point.split())
        point = []
        for fl in str_point:
            fl = float(fl)
            point.append(fl)
        a = tuple(point[:2])  # get tuple with (x,y)
        b = point[-1]         # get height z
        points.append([a,b])  # adding to array with all points [(y,x),z]
    return points

def getRowsFromPoints(points, quantity): #OK!
    '''function get point list and quantity elements from down line at x axis
    and returned list with lines from bottom to top
    '''
    temporaryRow = []
    rows = []
    for point in points:

        if len(temporaryRow) == quantity:
            rows.append(temporaryRow)
            temporaryRow = []
            temporaryRow.append(point)
        else:
            temporaryRow.append(point)
            if point == points[-1]:
                rows.append(temporaryRow)

    return rows

def getQuadsFromTwoRows(row1, row2): #OK!
    '''get two rows return all Quads from two Rows'''
    columns = list(zip(row1, row2))

    quad = []
    quads = []
    count = 0
    while count != len(columns):

        point1 = columns[count][0]
        point2 = columns[count][1]
        quad.append(point1)
        quad.append(point2)
        count += 1
        if len(quad) == 4:
            quads.append(quad)
            quad = []
            count -= 1
    return quads

def getAllQuads(rows): #OK!
    '''function returned two rows from rows Beginning from bottom to top'''
    all_quads = []
    two_rows = []
    count = 0
    row2 = None
    while row2 != rows[-1]: #warning
        row1 = rows[count]
        row2 = rows[count+1]
        quads_from_two_rows = getQuadsFromTwoRows(row1, row2)
        all_quads.extend(quads_from_two_rows)
        count += 1
    return all_quads


