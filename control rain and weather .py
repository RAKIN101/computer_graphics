from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

WINDOW_LEFT = 0
WINDOW_RIGHT = 600
WINDOW_BOTTOM = 0
WINDOW_TOP = 500

dn = [0.0, 0.0, 0.0]  
NUM_DROPS = 200
rain_speed = 5
rain_dx, rain_dy = 0, -1
rain_drops = []
rain = True


def iterate():
    glViewport(0, 0, 600, 550)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500.0, 0.0, 500.0, -1.0, 1.0)  
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()



def showScreen():
    glClearColor(dn[0], dn[1], dn[2], 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    # Background
    glBegin(GL_TRIANGLES)
    glColor3f(0.56, 0.44, 0.20)
    glVertex2d(500, 300)
    glVertex2d(0, 300)
    glVertex2d(0, 0)

    glVertex2d(500, 300)
    glVertex2d(0, 0)
    glVertex2d(500, 0)
    glEnd()

    # Trees
    for i in range(0, 500, 40):
        glBegin(GL_TRIANGLES)


        glColor3f(0.0, 0.4, 0.0)
        glVertex2d(i, 225)


        glColor3f(0.0, 0.9, 0.0)
        glVertex2d(i + 20, 285)


        glColor3f(0.0, 0.4, 0.0)
        glVertex2d(i + 40, 225)

        glEnd()


    # basha
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2d(400, 250)
    glVertex2d(100, 250)
    glVertex2d(100, 100)

    glVertex2d(400, 250)
    glVertex2d(100, 100)
    glVertex2d(400, 100)
    glEnd()

    # chal
    glBegin(GL_TRIANGLES)
    glColor3f(0.40, 0.0, 0.6)
    glVertex2d(250, 350)
    glVertex2d(50, 250)
    glVertex2d(450, 250)
    glEnd()

    # Door
    glBegin(GL_TRIANGLES)
    glColor3f(0.2588, 0.6667, 1.0)
    glVertex2d(300, 200)
    glVertex2d(225, 200)
    glVertex2d(225, 100)

    glVertex2d(300, 200)
    glVertex2d(225, 100)
    glVertex2d(300, 100)
    glEnd()

    # Windooo
    glBegin(GL_TRIANGLES)
    glColor3f(0.2588, 0.6667, 1.0)
    glVertex2d(175, 200)
    glVertex2d(125, 200)
    glVertex2d(125, 150)

    glVertex2d(175, 200)
    glVertex2d(125, 150)
    glVertex2d(175, 150)

    glVertex2d(375, 200)
    glVertex2d(325, 200)
    glVertex2d(325, 150)

    glVertex2d(375, 200)
    glVertex2d(325, 150)
    glVertex2d(375, 150)
    glEnd()

    # Windo bars
    glBegin(GL_LINES)
    glColor3f(0, 0.0, 0.0)
    glVertex2f(125, 175)
    glVertex2f(175, 175)
    glVertex2f(150, 200)
    glVertex2f(150, 150)

    glVertex2f(325, 175)
    glVertex2f(375, 175)
    glVertex2f(350, 200)
    glVertex2f(350, 150)
    glEnd()

    # knob
    glPointSize(7)
    glBegin(GL_POINTS)
    glColor3f(0, 0, 0)
    glVertex2f(275, 125)
    glEnd()

    drawRain()

    glutSwapBuffers()

def createRainDrops():
    
    for i in range(NUM_DROPS):
        x = random.uniform(-WINDOW_LEFT, WINDOW_RIGHT )
        y = random.uniform(WINDOW_BOTTOM, WINDOW_TOP)
        color = random.choice(['white', 'blue'])
        rain_drops.append([x, y, color])

def drawRain():
    glLineWidth(2)
    for drop in rain_drops:
        x, y, color = drop
        if color == 'white':
            glColor3f(1, 1, 1)
        else:
            glColor3f(0.2, 0.6, 1.0)
        glBegin(GL_LINES)
        glVertex2f(x, y)
        glVertex2f(x + rain_dx * 20, y + rain_dy * 20)
        glEnd()


def updateRain():    
    for drop in rain_drops:
        drop[0] += rain_dx * rain_speed
        drop[1] += rain_dy * rain_speed
        if drop[1] < WINDOW_BOTTOM  or drop[0] < WINDOW_LEFT  or drop[0] > WINDOW_RIGHT:
                drop[0] = random.uniform(WINDOW_LEFT-100, WINDOW_RIGHT)
                drop[1] = random.uniform(WINDOW_BOTTOM, WINDOW_TOP +500)
    glutPostRedisplay()





def keyboardListener(key, x, y):
    global dn, rain
    if key == b'w':
        dn = [min(1.0, dn[0] + 0.2),
              min(1.0, dn[1] + 0.2),
              min(1.0, dn[2] + 0.2)]
    elif key == b's':
        dn = [max(0.0, dn[0] - 0.2),
              max(0.0, dn[1] - 0.2),
              max(0.0, dn[2] - 0.2)]
    
   
    glutPostRedisplay()


def specialKey(key, x, y):
    global rain_dx, rain_dy, rain_speed

    if key == GLUT_KEY_UP:
        rain_speed = min(rain_speed + 5, 15)
    elif key == GLUT_KEY_DOWN:
        rain_speed = max(5, rain_speed - 5)
    elif key == GLUT_KEY_LEFT:
        rain_dx = max(rain_dx-.5,-1)
        rain_dy = -1
    elif key == GLUT_KEY_RIGHT:
        rain_dx = min(rain_dx+0.5,1)
        rain_dy = -1
    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(600, 550)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"OpenGL Coding Practice")

glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKey)
glutIdleFunc(updateRain)

createRainDrops()
glutMainLoop()
