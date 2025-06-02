class VolunteerEncryptedData:
    def __init__(self, volunteerId, clueHowToDecrypt, ciphertext):
        self.volunteerId = volunteerId # must match the id of an instance of `Volunteer` 
        self.clueHowToDecrypt= clueHowToDecrypt
        self.ciphertext = ciphertext
        '''
            e.g.    {
                    "name": {
                            "family_name":  "Doe",
                            "given_name":   "John",
                            "other_names":  "middle, maiden, nick-, etc."
                            },
                    "contact":  {
                                "phone": "",
                                "email: "",
                                "street":"",
                                "other":    {
                                            "social_media": ""
                                            }
                                },
                    "ids_of_projects_worked_on":[1,2,3],
                    "ids_of_awards_received":[4,5],
                    "ideas_for_fun_thank_you_gifts": ""
                    }
        '''
