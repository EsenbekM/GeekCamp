class Employer:

    name = "Islam"
    age = 17
    contact = "077777777"
    color = 'Black'

    def work(self):
        print("БЫТЬ РАБОМ")


class Developer(Employer):

    def work(self):
        print("ТИПО ПИШЕТ КОД,,,")


p1 = Employer()
p1.work()

p2 = Developer()
p2.work()

