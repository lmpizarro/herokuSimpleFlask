class Contacts():
    def __init__(self):
        self.contacts =[]
        pass


    def add_contact (self, name, email, telefono, mensaje):
        self.contacts.append ({'nombre':name, 'email':email, 'phone':telefono, 'mensaje':mensaje}) 
        print name, email, telefono, mensaje
