from datetime import date

from django.db import models


# import jsonfield
#from phonenumber_field.modelfields import PhoneNumberField

# Create Part model with necessary attributes



# class eventLog(models.Model):
#     checkedOutTo = models.ForeignKey('User', null=True, related_name='checkedOutTo', on_delete=models.CASCADE)
#     checkedOutBy = models.ForeignKey('User', null=True, related_name='checkedOutBy', on_delete=models.CASCADE)
#     logType = models.CharField(null=False, max_length=200)
#     content = jsonfield.JSONField()

class Part(models.Model):
    part = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    quantity_Checked_Out = models.IntegerField(default=0)
    id_Number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.part

# Create User model with necessary attributes
class User(models.Model):

    # def __init__(self, *args, **kwargs):
    #     super(User, self).__init__(*args, **kwargs)
    #
    #     self.createUserType()

    # def save(self, *args, **kwargs):
    #     super(User, self).__init__(*args, **kwargs)
    #
    #     self.createUserType()

    MEMBER_TYPE = (
        ('MEMBER', 'MEMBER'),
        ('ADMIN', 'ADMIN'),
        ('MEMBER_EXPIRED', 'MEMBER EXPIRED'),
        ('NON_MEMBER', 'NON MEMBER'),
        ('OFFICER', 'OFFICER'),
    )
    userType = models.CharField(
        max_length=50,
        choices=MEMBER_TYPE,
        default=('MEMBER', 'MEMBER'),
    )
    first_Name = models.CharField(max_length=500)
    last_Name = models.CharField(max_length=500)
    # user_Type = models.CharField(max_length=100, default="STUDENT")
    cal_Poly_Email = models.EmailField(null=False, max_length=500, unique=True)
    ieee_member_number = models.CharField(null=True, max_length=500, blank=True, unique=True)
    ieee_member_expiration_date = models.DateField(null=True, blank=True)
    phone_Number = models.CharField(max_length= 100, null=True, blank=True)
    polyCard_Data = models.CharField(max_length=500, null=True, blank=True, unique=True)
    # library_Code_Number = models.IntegerField(default=0)
    # iso_Number = models.IntegerField(default=0)
    parts                 = models.ManyToManyField(Part, blank=True)
    has_Items_Checked_Out = models.BooleanField(default=False, blank=True)
    is_super = models.BooleanField(default=False, blank=True)

    # createUserType()

    def createUserType(self, *args, **kwargs):
        if self.is_super is False:
            print("NON ADMIN ACCOUNT")
            if self.ieee_member_number is not "":
                try:
                    print(date.today())
                    if date.today() > self.ieee_member_expiration_date:
                        print("Change membership to expired")
                        self.userType = 'MEMBER_EXPIRED'

                    else:
                        print("Change membership to MEMBER")
                        self.userType = 'MEMBER'
                except TypeError:
                    print("Could not compute time delta")
                    self.userType = 'NON_MEMBER'
                    pass
            else:
                print("userTypeTTest")
                self.userType = 'NON_MEMBER'
            print("SAVE USER")
            self.save(update_fields=["userType"])


    def clean(self, *args, **kwargs):
        super(User, self).clean(*args, **kwargs)
        # print (email)
        # if not email.endswith('@calpoly.edu'):
        #     raise ValidationError('Domain of email is not valid')
        # self.validate_email()

    # def validate_email(self):
    #     email = self.cal_Poly_Email
    #
    #     if not email.endswith('@calpoly.edu'):
    #         raise ValidationError('Domain of email is not valid')
    #
    #     return email

    def __str__(self):
        # return self.__dict__
        return self.first_Name + ' ' + self.last_Name

class userPart(models.Model):
    # userAssigned = models.EmailField(null=True, max_length=100)
    userAssigned = models.ForeignKey('User', null=True, related_name='userAssigned', on_delete=models.CASCADE)
    #userAssigned = User()
    part = models.CharField(max_length=100)
    quantity_Checked_Out = models.IntegerField(default=0)
    id_Number = models.CharField(blank=True, null=True, default=0000, max_length=200)

    def __str__(self):
        return self.part


# Create Transaction model with necessary attributes
# We'll worry about this later...
# What is the difference between transaction and log
# class Transaction(models.Model):
#     # userid
#     # part
#     # date
#     pass

# Create Lab model with necessary attributes


# class Lab(models.Model):
#     course_Name_Text = models.CharField(max_length=100)
#     section_Number = models.IntegerField(default=0)
#     experiment_Number = models.IntegerField(default=0)
#     parts = models.ManyToManyField(Part)
    # possible things to add: professor name

# Create Log model with necessary attributes

#
# class Log(models.Model):
#     #date_And_Time = models.DateTimeField(
#     #    default=datetime.datetime.now(), blank=True)
#     client_Name_Text = models.CharField(max_length=100)
#     tech_Name_Text = models.CharField(max_length=100)
#     parts = models.ManyToManyField(Part)
#     transaction_Complete = models.BooleanField(default=False)
