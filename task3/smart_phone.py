class phone:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        if name in self.contacts:
            print(f"{name} is already in the phone book.")
        else:
            self.contacts[name] = number
            print(f"Added {name} to the phone book.")

    def remove_contact(self, name):
        if name not in self.contacts:
            print(f"{name} is not in the phone book.")
        else:
            self.contacts.pop(name)
            print(f"Removing {name} from the phone book.")

    def make_call(self, name):
        if name not in self.contacts:
            print(f"{name} is not in the phone book.")
        else:
            print(f"Calling {name}...")


class camera:
    def __init__(self):
        pass

    def take_picc(self):
        print("The picture was taken successfully")


class smartphone(phone, camera):
    def __init__(self):
        phone.__init__(self)
        camera.__init__(self)


if __name__ == "__main__":
    my_phone = smartphone()
    my_phone.add_contact("hamada", "0127654321")
    my_phone.add_contact("omer", "0112345678")
    my_phone.make_call("hamada")
    my_phone.take_picc()
    my_phone.remove_contact("hamada")
    my_phone.make_call("hamada")
