from OpenGL.GL import *
from glew_wish import *
import glfw

xObstaculo = 0.0
yObstaculo = 0.0

xCarrito = 0.0
yCarrito = 0.0

colisionando = False

def checar_colisiones():
    
    global colisionando

    #los laditos--------------------
    #Si extreDerechaCarrito > extreIzqObstaculo
    #Y extreDerechaCarrito < extreIzqObstacu


    if xCarrito +0.05 > xObstaculo -0.15 and  xCarrito -0.05 < xObstaculo and yCarrito +0.05 > yObstaculo - 0.15 and yCarrito - 0.05< yObstaculo + 0.15:
        colisionando = True
    else:
        colisionando = False

    #eje y ----------------------------------
    #si ext superiorCarrirto > ExtrInferior obstaculo
    #y extremoinferiorcarrito <extresmsuperior obstaculo

def actualizar(window):

    global xCarrito 
    global yCarrito


    estadoIzq = glfw.get_key(window, glfw.KEY_LEFT)
    estadoDer = glfw.get_key(window, glfw.KEY_RIGHT)
    estadoArriba = glfw.get_key(window, glfw.KEY_UP)
    estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)

    if estadoIzq == glfw.PRESS:
        xCarrito -=  0.0035
    if estadoDer == glfw.PRESS:
        xCarrito +=  0.0035
    if estadoAbajo == glfw.PRESS:
        yCarrito -= 0.0035
    if estadoArriba == glfw.PRESS:
        yCarrito += 0.0035

    checar_colisiones()

def dibujarCarrito():

    global xCarrito
    global yCarrito
    global colisiones

    glPushMatrix()
    glTranslate( xCarrito, yCarrito , 0.0)
    glBegin(GL_TRIANGLES)
    if colisionando == True:
        glColor3f(0.4,0.8,0.1)
    else:
        glColor3f(0.0,0.0,0.0)

    glVertex3f(0.0,0.015,0.0)
    glVertex3f(-0.015,-0.015,0.0)
    glVertex3f(0.015,-0.015,0.0)
    

    glEnd()
    glPopMatrix()



def dibujarObstaculo():

    global xObstaculo
    global yObstaculo 

    glPushMatrix()
    glTranslate(xObstaculo, yObstaculo, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.8,1.0,1.1)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.00, 0.15,0.0)
    glVertex3f(0.00,-0.15,0.0)
    glVertex3f(-0.15, -0.15,0.0) 
    glEnd()
    glPopMatrix()


def paredes1():
    glPushMatrix()
    glTranslate(xObstaculo, yObstaculo, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,0.0)
    glVertex3f(-0.1,0.35,0.0)
    glVertex3f(-0.15, 0.35,0.0)
    glVertex3f(-0.15,-0.0,0.0)
    glVertex3f(-0.1, -0.0,0.0) 
    glEnd()
    glPopMatrix()

    

def paredes2():
    glPushMatrix()
    glTranslate(xObstaculo, yObstaculo, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,0.0)
    glVertex3f(0.05,-0.07,0.0)
    glVertex3f(0.05,-0.20,0.0)
    glVertex3f(-0.2,-0.20,0.0)
    glVertex3f( -0.2,-0.07,0.0) 
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.001, -0.1, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.05, 0.0, 0.0)
    glVertex3f(0.05, 0.2, 0.0)
    glVertex3f(0.0, 0.2, 0.0)
    glEnd()
    glPopMatrix()

def paredes3():
    glPushMatrix()
    glTranslate(xObstaculo, yObstaculo, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0,.0,0.0)
    glVertex3f(0.05,0.05,0.0)
    glVertex3f(0.05,0.20,0.0)
    glVertex3f(-0.2,0.20,0.0)
    glVertex3f( -0.2,0.05,0.0) 
    glEnd()
    glPopMatrix()       

def paredes():
    glPushMatrix()
    glTranslate(xObstaculo, yObstaculo, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,0.0)
    glVertex3f(-0.05,0.5,0.0)
    glVertex3f(0.05, 0.5,0.0)
    glVertex3f(0.05,-0.5,0.0)
    glVertex3f(-0.05, -0.5,0.0) 
    glEnd()
    glPopMatrix()

def caminos():
    glPushMatrix()
    glTranslate(-0.5, 0.01, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.04, 0.0)
    glVertex3f(0.4, 0.04, 0.0)
    glVertex3f(0.4, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.6, -0.1, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.04, 0.0)
    glVertex3f(0.5, 0.04, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.5, 0.05, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.4, 0.0)
    glVertex3f(0.0, 0.4, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.6, -0.1, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.55, 0.0)
    glVertex3f(0.0, 0.55, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.5, 0.45, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.04, 0.0)
    glVertex3f(0.6, 0.04, 0.0)
    glVertex3f(0.6, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.76, 0.45, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.04, 0.0)
    glVertex3f(0.2, 0.04, 0.0)
    glVertex3f(0.2, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.85, 0.56, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.04, 0.0)
    glVertex3f(0.95, 0.04, 0.0)
    glVertex3f(0.95, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.5, 0.34, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.04, 0.0)
    glVertex3f(0.6, 0.04, 0.0)
    glVertex3f(0.6, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.4, 0.15, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.2, 0.0)
    glVertex3f(0.0, 0.2, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.295, 0.01, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.2, 0.0)
    glVertex3f(0.0, 0.2, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.298, 0.28, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.08, 0.0)
    glVertex3f(0.0, 0.08, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.2, 0.2, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.08, 0.0)
    glVertex3f(0.0, 0.08, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.2, 0.25, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.04, 0.0)
    glVertex3f(0.58, 0.04, 0.0)
    glVertex3f(0.58, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.17, 0.25, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.43, 0.0)
    glVertex3f(0.0, 0.43, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.27, 0.35, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.25, 0.0)
    glVertex3f(0.0, 0.25, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.3, 0.45, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.04, 0.0)
    glVertex3f(0.2, 0.04, 0.0)
    glVertex3f(0.2, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.38, 0.14, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.25, 0.0)
    glVertex3f(0.0, 0.25, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.3, 0.56, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.04, 0.0)
    glVertex3f(0.2, 0.04, 0.0)
    glVertex3f(0.2, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.5, -0.01, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.5, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.5, 0.56, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.25, 0.0)
    glVertex3f(0.0, 0.25, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.19, 0.099, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.04, 0.0)
    glVertex3f(0.23, 0.04, 0.0)
    glVertex3f(0.23, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.22, -0.01, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.04, 0.0)
    glVertex3f(0.3, 0.04, 0.0)
    glVertex3f(0.3, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.19, -0.5, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.53, 0.0)
    glVertex3f(0.0, 0.53, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.1, -0.4, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.68, 0.0)
    glVertex3f(0.0, 0.68, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.25, 0.2, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.08, 0.0)
    glVertex3f(0.0, 0.08, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.012, -0.5, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.04, 0.0)
    glVertex3f(0.18, 0.04, 0.0)
    glVertex3f(0.18, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.01, -0.5, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.23, 0.0)
    glVertex3f(0.0, 0.23, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.6, -0.29, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.04, 0.0)
    glVertex3f(0.65, 0.04, 0.0)
    glVertex3f(0.65, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.31, -0.252, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.08, 0.0)
    glVertex3f(0.0, 0.08, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.41, -0.178, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.08, 0.0)
    glVertex3f(0.0, 0.08, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.51, -0.252, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.08, 0.0)
    glVertex3f(0.0, 0.08, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.76, -0.178, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.04, 0.0, 0.0)
    glVertex3f(0.04, 0.65, 0.0)
    glVertex3f(0.0, 0.65, 0.0)
    glEnd()
    glPopMatrix()

    


def dibujar():
    caminos()
    paredes3()
    paredes2()
    #paredes1()
    #paredes()
    dibujarObstaculo()
    dibujarCarrito()






def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0.8,1.0,1.1,2)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        actualizar(window)
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()