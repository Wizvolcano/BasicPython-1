class Car():
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def security(self):
        print(f'รถยี่ห้อ: {self.brand}')
        print(f'รุ่น: {self.model}')

    def drive(self):
        print('ห้ามใช้เส้นทางนี้')

    def park(self):
        print('เชิญที่จอดรถทั่วไป')

class SuperCar(Car):

    def __init__(self, brand, model, engine):
        super().__init__(brand, model)
        self.engine = engine
    
    def drive(self):
        print('ขับตรงไปได้')
    
    def park(self):
        print('เชิญที่จอดรถ Super Car')

if __name__ == '__main__':
    car1 = Car('Toyota', 'Camry')
    car2 = Car('Honda', 'Accord')
    car3 = SuperCar('Lamborghini', 'Aventador', 'V.12')
    car4 = SuperCar('Ferrari', 'Italia 459', 'V.12')

    print('ณ ห้างสรรพสินค้าแห่งหนึ่ง')
    car1.security()
    car1.drive()
    car1.park()
    print('---------')
    car3.security()
    car3.drive()
    car3.park()
    print('---------')





