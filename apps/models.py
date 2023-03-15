from django.db.models import Model, CharField, ForeignKey, CASCADE, ImageField


class Jobs(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Address(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Customer(Model):
    name = CharField(max_length=255)
    phone_number = CharField(max_length=244)
    email = CharField(max_length=255)
    address = ForeignKey(Address, on_delete=CASCADE)
    jobs = ForeignKey(Jobs, on_delete=CASCADE)
    image = ImageField(upload_to="%m")



    def __str__(self):
        return self.name
