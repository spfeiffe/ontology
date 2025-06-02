class Volunteer:
    def __init(self, id, emergency_contact, pointerToEncryptedData):
        self.id = id
        self.emergency_contact = emergency_contact
        '''
        e.g.    {
                "emergency_contact_name": "Jane Roe",
                "emergency_contact_phone": "(123) 456-7890"
                }
        '''
        self.pointerToEncryptedData = pointerToEncryptedData
