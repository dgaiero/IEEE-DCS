from polyCardData import getData
from app_Transaction.models import User


def checkRegistrationStatus(polyCardText):

    polyData = getData(polyCardText)
    if(polyData is not None):
        isoNumber = polyData['isoNumber']
        libraryCode = polyData['libraryCode']
        try:
            User.objects.get(iso_Number=isoNumber)
        except DoesNotExist:
            return "User does not exist"


def RegisterUser(userFirstName, userLastName, userEMail, isoNumber, libraryCodeNumber):
    newUser = User(first_Name_Text=userFirstName, last_Name_Text=userLastName, user_Type_Text="STUDENT",
                   user_Email=userEMail, iso_Number=isoNumber, library_Code_Number=libraryCodeNumber)
    newUser.save()
