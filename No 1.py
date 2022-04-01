# Anggelina Kismasari 20051397034
# B Algoritma Garis Brenseham
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def initFun():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(128.0,0.0, 0.0)
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,640.0,0.0,480.0)
    
def AlgDDA():
    x1 = 20
    y1 = 20
    x2 = 500
    y2 = 400
    x = x1
    y = y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    p = 2 * dy - dx
    duady = 2 * dy
    duadydx = 2 * (dy - dx)
    
    if (x1 > x2):
        x = x2
        y = y2
        xend = x1
    else:
        x = x1
        y = y1
        xend = x2
    
    glBegin(GL_POINTS)
    glVertex2i(x, y)

    while (x < xend):
        x = x+1
        if (p < 0):
            p += duady
        else:
            if (y1 > y2):
                y = y-1
            else:
                y = y+1
            p += duadydx
        glVertex2i(x, y)

    glEnd()
    glFlush()

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640,480)
    glutCreateWindow("UTS GRAFIKA KOMPUTER")
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutDisplayFunc(AlgDDA)
    initFun()