from OpenGL.GL import *
from glew_wish import *
import glfw

xLaberinto1 = 0.0
yLaberinto1 = 0.0

xCarrito = 0.0
yCarrito = 0.0

colisionando = False

def checar_colisiones():
    
    global colisionando

    #los laditos--------------------
    #Si extreDerechaCarrito > extreIzqLaberinto1
    #Y extreDerechaCarrito < extreIzqObstacu


    if xCarrito +0.05 > xLaberinto1 -0.15 and  xCarrito -0.05 < xLaberinto1 and yCarrito +0.05 > yLaberinto1 - 0.15 and yCarrito - 0.05< yLaberinto1 + 0.15:
        colisionando = True
    else:
        colisionando = False

    #eje y ----------------------------------
    #si ext superiorCarrirto > ExtrInferior Laberinto1
    #y extremoinferiorcarrito <extresmsuperior Laberinto1




        



def actualizar(window):

    global xCarrito 
    global yCarrito


    estadoIzq = glfw.get_key(window, glfw.KEY_LEFT)
    estadoDer = glfw.get_key(window, glfw.KEY_RIGHT)
    estadoArriba = glfw.get_key(window, glfw.KEY_UP)
    estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)

    if estadoIzq == glfw.PRESS:
        xCarrito -=  0.01
    if estadoDer == glfw.PRESS:
        xCarrito +=  0.01
    if estadoAbajo == glfw.PRESS:
        yCarrito -= 0.01
    if estadoArriba == glfw.PRESS:
        yCarrito += 0.01

    checar_colisiones()


def dibujarLaberinto1():

    global xLaberinto1
    global yLaberinto1 

    glPushMatrix()
    glTranslate(xLaberinto1, yLaberinto1, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,1.0)
    glVertex3f(-8.0,0.30,0.0)
    glVertex3f(0.0, 0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-8.0, -0.30,0.0) 
    glEnd()
    glPopMatrix()

def dibujarCarrito():

    global xCarrito
    global yCarrito
    global colisiones

    glPushMatrix()
    glTranslate( xCarrito, yCarrito , 0.0)
    glBegin(GL_TRIANGLES)
    if colisionando == True:
        glColor3f(1.0,1.0,1.0)
    else:
        glColor3f(1.0,0.0,0.0)

    glVertex3f(0.0,0.05,0.0)
    glVertex3f(-0.05,-0.05,0.0)
    glVertex3f(0.05,-0.05,0.0)
    

    glEnd()
    glPopMatrix()

def dibujar():
    dibujarLaberinto1()
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
        glClearColor(0.4,0.8,0.1,1)
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