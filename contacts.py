class Contacts():
    def __init__(self):
        self.contacts =[]
        pass


    def add_contact (self, name, email, telefono, mensaje):
        self.contacts.append ({'nombre':name, 'email':email, 'phone':telefono, 'mensaje':mensaje}) 
        #print name.decode("utf-8"), email.decode("utf-8"), telefono.decode("utf-8"), mensaje.decode("utf-8")
