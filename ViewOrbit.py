import pygame as pg
import math 

""" Все материальные точки будут двигатся в силовом поле тяжести """
""" Пока что для простоты центральное поле будет пораждатся каким то одним телом """

""" Вспомогательные функции """ 

def norm( y : list[float] ) -> float:
    pass

def normalize( y : list[float] ) -> list[float]:
    norm_ = norm(y)
    return [ x / norm_ for x in y ]

def getArg( x : list[float] ) -> float:
    return math.atan( x[0] / x[1] )

def vectorScale( scale : float, y : list[float] ) -> list[float]:
    return [ x * scale for x in y ]
    
""" Вспомогательные функции """ 
 
""" Материальная точка """
class MaterialPoint:
    
    def __init__(self, mass : float, coords : list[float]):
        self.mass = mass
        self.coords = coords
    
    def doPhysics():
        pass

""" Сила """
class Force:
    
    def __init__(self, direction : list[float], matPoint : MaterialPoint):
        self.direction = direction
        self.materialPoint = matPoint

    def __call__(self, coords : list[float] ):
        pass

""" Силовое поле """
class ForceField:
    def __init__(self, force : Force):
        self.force = force
    
    def draw(self, screen):
        w = screen.w
        h = screen.h
        
        stepX, stepY = 1, 1
        x, y = 0, 0
        scale = 0.5
        
        while x < w:
            x = 0
            while y < h:
                vec = self.force([x,y]) # вектор силы в точке x,y
                vec = normalize(vec)
                
                A = (x,y)
                B = (x + vec[0], y + vec[1])
                
                pg.draw.line( screen, [255,255,255], A, B )
                
                x += stepX
            y += stepY
                

""" Настройки интегрирования """
class IntegrationSettings:
    
    def __init__(self, startT : float, step : float, startCoords : list[float]):
        self.step = step
        self.start = startT
        self.startCoords = startCoords
       
""" Простой прогноз """ 
class SimpleMotion:
    
    def __init__(self, integratinSettings : IntegrationSettings):
        self.integSettings = integratinSettings
        self.currentTime = 0
        
    def stepTo(self, dt):
        pass
    
def scale():
    pass    

def drawOrbit( screen ):
    pass

def drawMaterialPoint( screen ):
    pass

def mainLoop():
    earth = MaterialPoint(1e10, [1,1,1,1,1,1])


screen = pg.display.set_mode([500, 500])
pg.init()
screen.fill((255, 255, 255))
