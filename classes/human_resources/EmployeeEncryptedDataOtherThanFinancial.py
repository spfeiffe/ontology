class EmployeeEncryptedDataOtherThanFinancial:
    def __init__(self, employeeId, clueHowToDecrypt, ciphertext):
        self.employeeId = employeeId # must match the id of an instance of `Employee` 
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
                                            "ORCID": "",
                                            "social_media": ""
                                            }
                                },
                    "expertise_keywords":   {
                                            "key":"value"
                                            },
                    "optional": {
                                "ids_of_projects_worked_on":[1,2,3],
                                "ids_of_awards_received":[4,5],
                                "fun_facts":["champion_knitter", "etc."],
                                "voluntary_demographic_data":{}
                                }
                    }
        '''
