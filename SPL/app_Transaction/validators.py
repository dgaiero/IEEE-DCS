from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_domainonly_email(value):
    """
    Let's validate the email passed is in the domain "calpoly.edu"
    """
    if not "calpoly.edu" in value:
        raise ValidationError(_("Sorry, the email submitted is invalid. All emails have to be registered on this domain only."))
