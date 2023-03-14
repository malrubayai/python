# The Contact class holds contact information.

class Contact:
    # The __init__method initializes the attributes.
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    # set_name method sets the name attribute.
    def set_name(self, name):
        self.__name = name

    # The set_phone method sets the phone attibute.
    def set_phone(self, phone):
        self.__phone = phone

    # The set_phone method sets the email attibute.
    def set_email(self, email):
        self.__email = email

    # The get_name method returns the name attibute.
    def get_name(self):
        return self.__name

    # The get_phone method returns the phone attibute.
    def get_phone(self):
        return self.__phone

    # The get_email method returns the email attibute.
    def get_email(self):
        return self.__email

    # The __str__ methos returns the object's state
    # as a string.
    def __str__(self):
        return "Name :" + self.__name + \
               "\nPhone: " + self.__phone + \
               "\nEmail " + self.__email
