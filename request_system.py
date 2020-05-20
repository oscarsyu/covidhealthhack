
class getRecords
    def __init__(self):


    class Record
        def __init__(self, user_info, bank_info, benefits):
            name = user_info[""]

            routing_number = bank_info["routing_number"]
            account_number =
            monthly_check

    #instead of object, maybe have function that grabs from object in the code_sending system
    def pull_record(employer_id, employee_code):
        """pulls data for 1 employee in 1 employer"""

        #code to pull data
        #return as a tuple

    def employer_request_records(employer_id, employee_codes):
        '''pulls data from database of employee benefits
        '''
        all_employee_info = []
        for c in employee_codes:
            bank_info = ...
            benefits = ...
            employee_info = (bank_info, benefits, )
            all_employee_info.append()
        #return as a list of tuples
