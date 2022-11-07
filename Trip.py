# class Trip:
#     def __init__(self,trip_cities,aircraft,price,start_date,route=''):
#         self.trip_cities=trip_cities
#         self.start_date=start_date
#         self.aircraft=aircraft
#         self.trip_route=route
#         self.price=price

#     def __repr__(self):
#         return f'Trip:{self.trip_cities} Aircraft:{self.aircraft} route:{self.trip_route} price:{self.price}'

class A:
    def __init__(self,x):
        self.x = x
    def count(self,x):
        self.x = self.x+1
class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
    def count(self):
        self.y += 1     
def main():
    obj = B()
    obj.count()
    print(obj.x, obj.y)
main()