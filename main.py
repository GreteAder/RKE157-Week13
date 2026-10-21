from animal import Animal, Cat, Dog

my_cat = Cat("Fluffy")
my_dog = Dog("Rex")

neighbor_dog = Dog("Buddy")

my_dog.dog_sees(neighbor_dog)
my_dog.dog_sees(my_cat)
my_cat.cat_sees(my_dog)