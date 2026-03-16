class User:
    def __init__(self, first_name, last_name, age, email, status):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.status = status

    def describe_user(self):
        print("Nama:", self.first_name, self.last_name)
        print("Umur:", self.age)
        print("Email:", self.email)
        print("status:", self.status)

    def greet_user(self):
        print("Halo", self.first_name + "! Selamat datang kembali.")
    def greet_user2(self):
        print("hai", self.first_name + "lama tidak bertemu")
    


# Membuat beberapa instance user
user1 = User("Wahyu", "Hidayah", "19 tahun", "wahyu@email.com", "Belum Menikah")
user2 = User("Siti", "Asya", "17 tahun", "siti@email.com", "Belum Menikah")
user3 = User("habibur", "ridho", "20 tahun", "ridho@gmail.com", " Sudah Menikah")

user1.describe_user()
user1.greet_user()
print()

user2.describe_user()
user2.greet_user2()
print()

user3.describe_user()
user3.greet_user()
