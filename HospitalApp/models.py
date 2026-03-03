from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100) #CharField is used to store string data, and max_length is a required argument that specifies the maximum length of the string.
    age = models.IntegerField() #IntegerField is used to store integer data, and it does not require a max_length argument.
    email = models.EmailField() #EmailField is used to store email addresses, and max_length is a required argument that specifies the maximum length of the email address.
    gender = models.CharField(max_length=10) #CharField is used to store string data, and max_length is a required argument that specifies the maximum length of the string.
    phone_number = models.CharField(max_length=16) #CharField is used to store string data, and max_length is a required argument that specifies the maximum length of the string.
    date_of_birth = models.DateField() #DateField is used to store date data, and it does not require a max_length argument.
    date_and_time_of_admission = models.DateTimeField() #DateTimeField is used to store date and time data, and it does not require a max_length argument.
    medical_history = models.TextField() #TextField is used to store large text data, and it does not require a max_length argument.

    def __str__(self):
        return self.name #The __str__ method is a special method in Python that is used to define the string representation of an object. In this case, it returns the name of the patient when the object is printed or converted to a string. Onlu used as string representation of the object, it does not affect the functionality of the model.
