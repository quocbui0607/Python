class SuperSaiyan():
    power = 50

    @classmethod
    def update_power_cls(cls, new_power):
        cls.power = new_power

    def update_power_no_cls(self, new_power):
        self.power = new_power


goku = SuperSaiyan()
print("sức mạnh của Saiyan: ", SuperSaiyan.power)
print("sức mạnh của goku: ", goku.power)

print('\nKhông dùng class method')
goku.update_power_no_cls(30)
print("sức mạnh của Saiyan: ", SuperSaiyan.power)
print("sức mạnh của goku: ", goku.power)

print('\nDùng class method')
goku.update_power_cls(30)
print("sức mạnh của Saiyan: ", SuperSaiyan.power)
print("sức mạnh của goku: ", goku.power)