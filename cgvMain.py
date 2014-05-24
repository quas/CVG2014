#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import cgvLeicaXmlReader
import cgvMath

# xml_file = 'SquareWith65.xml'
xml_file = 'SquareWith78.xml'
points = cgvLeicaXmlReader.getPointsFromXmlFile(xml_file)
length_of_points = len(points)
QUANTITY_POINTS_AT_X_AXIS = 13
STATIC_HEIGHT = -22.00
rows = cgvLeicaXmlReader.getRowsFromPoints(points, QUANTITY_POINTS_AT_X_AXIS)
quads = cgvLeicaXmlReader.getAllQuads(rows)

volumes = []

for quadrangle in quads:
    Quadrangle_type = cgvMath.getTypeQuadrangle(quadrangle)
    v = cgvMath.getVolumeQuadrangle(quadrangle, Quadrangle_type, STATIC_HEIGHT)
    volumes.append(v)

print('При обработке поля из {0} точек, '
      'было собрано {1} четырехугольников, общий объем '
      'которых: {2}'.format(len(points), len(quads), round(sum(volumes), 3)))

