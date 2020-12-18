class Vector():
    def __init__(self, x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norm(self):#Длина вектора
            return (self.x ** 2 + self.y ** 2) ** 0.5

    def sum(self, b):#Сумма векторов
        xx = self.x - b.x
        yy = self.x - b.y
        zz = self.x - b.z
        return Vector(xx, yy, zz)
    def multiplyscalar(self, b):#Умножение скалярное
            ss = self.x * b.x + self.y * b.y + self.z * b.z
            return ss
    def multiplyvector(self,b):#Умножение векторное
        xx=self.y*b.z-self.z*b.y
        yy=self.x*b.z-self.z*b.x
        zz=self.x*b.y-self.y*b.x
        return Vector(xx, yy, zz)
    def multiplynumber(self,b):#Умножение вектора на число
        return Vector(self.x*b, self.y*b, self.z*b)
    def findnormalvector(self):#Найти вектор перпедикулярный данному
        if self.z!=0:
         return Vector(1,1,(-self.y -self.x)/self.z)
        elif self.x!=0:
         return Vector((-self.y -self.z)/self.x,1,1)
        elif self.y!=0:
            return Vector(1, (-self.x - self.z) / self.y, 1)
    def cosangele(self,b):#Найти угол между векторами
        return self.multiplyscalar(b)/(self.norm()*b.norm())
    def normilize(self):#Номализировать вектор
        return Vector(self.x/self.norm(),self.y/self.norm(),self.z/self.norm())
