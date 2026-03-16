class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("Nama Restoran:", self.restaurant_name)
        print("Jenis Masakan:", self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " sekarang buka!")
    def open_restaurant2(self):
        print(self.restaurant_name + "sekarang tutup!")
    def open_restaurant3(self):
        print(self.restaurant_name + "sedang istirahat")
        

# Membuat 1 instance
restaurant = Restaurant("Ampera Kito", "Padang")

# Panggil method
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()


# Membuat 3 instance berbeda
resto1 = Restaurant("Pizza Hut", "Italian")
resto2 = Restaurant("Sushi Tei", "Japanese")
resto3 = Restaurant("KFC", "Fast Food")

resto1.describe_restaurant()
resto1.open_restaurant2()
print()
resto2.describe_restaurant()
resto2.open_restaurant3()
print()
resto3.describe_restaurant()