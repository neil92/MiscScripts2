pi = 3.14159

class Disk:
    """
    Attributes:
        center: Point, the center of the disk
        radius: float, the radiusof the disk
        area: float, the area of the disk
        circ: float, the  circumference of the disk
        
    """
    def __init__(self,P,r):
        """ Creates a Disk object with center P and radius r
        PreC: P is a Point and r is a positive float
        """
        self.center = P
        self.radius = r
        self.area = pi*r**2
        self.circ = 2*pi*r
		
diskArray = []

for i in range(0, 10):
	diskArray.append(Disk(1,i))
	print diskArray[i].area