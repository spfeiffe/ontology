class ContractorEncryptedDataOtherThanFinancial:
    def __init__(self, contractorId, clueHowToDecrypt, ciphertext):
        self.contractorId = contractorId # must match the id of an instance of `Contractor` 
        self.clueHowToDecrypt= clueHowToDecrypt
        self.ciphertext = ciphertext
        '''
            e.g.    {
                    "name": {
                            "family_name":  "Doe",
                            "given_name":   "John",
                            "other_names":  "middle, maiden, nick-, etc."
                            },
                    "companyName": "GDIT",
                    "companyEmployeeId": "123",
                    "title": "Systems Engineer",
                    "contractData": {
                                    "contractNumber":"ab123hf", # must match the attribute `number` of an instance of `Contract` 
                                    "contractDuration": "1 year",
                                    etc.
                                    }
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
                    "ids_of_projects_worked_on":[1,2,3],
                    }
        '''
