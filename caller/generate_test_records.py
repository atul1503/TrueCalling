from caller.models import UserPhoneLabelMapping
from django.contrib.auth import get_user_model

# Assuming `PhoneUser` is your custom user model
PhoneUser = get_user_model()

class UserPhoneLabelMappingRecords:
    @classmethod
    def run(cls):
        UserPhoneLabelMapping.objects.create(fullname="Atul Tripathi",username="atultrip555", phonenumber="12345678910", label="VERIFIED")
        UserPhoneLabelMapping.objects.create(fullname="John Doe", phonenumber="1234567891", label="VERIFIED")
        UserPhoneLabelMapping.objects.create(fullname="Bharat Atul Aryan John", username="bharat_atul_aryan", phonenumber="1234567896", label="SPAM")
        UserPhoneLabelMapping.objects.create(fullname="Diana white",phonenumber="12345678910", label="SPAM")

        PhoneUser.objects.create(username="atultripa555",phonenumber="12345678910",password="wierdMan")
        

