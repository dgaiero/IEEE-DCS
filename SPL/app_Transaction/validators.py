from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_domainonly_email(value):
    """
    Let's validate the email passed is in the domain "calpoly.edu"
    """
    if not "calpoly.edu" in value:
        raise ValidationError(_("Sorry, the email submitted is invalid. All emails have to be registered on this domain only."))


def validate_polyCard(value):
    if (len(value) == 41 and
            value[0] == '%' and
            value[14] == '^' and
            value[15:22] == 'STUDENT' and
            value[22] == '?' and
            value[23] == ';' and
            value[40] == '?'):

        # Extracts useful info from PolyCard and stores in a dictionary
        library_Code_Number = int(value[1:14])
        iso_Number = int(value[24:40])
        useful_polyCard_Data = {'libraryCodeNumber': library_Code_Number,
                                'isoNumber': iso_Number,
                                }
        # return True
    else:
        # Returns 'None' if card is invalid
        raise ValidationError(
            _("Please swipe card again."))
