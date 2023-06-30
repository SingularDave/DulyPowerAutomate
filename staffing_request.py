from datetime import datetime, timedelta
from typing import List


class StaffingRequest:
    def __init__(self, manager_name: str, manager_email: str, clinic: str, request_type: str, start_time: datetime, end_time: datetime):

        if not isinstance(manager_name, str):
            raise TypeError("Manager name should be a string.")

        if not isinstance(manager_email, str):
            raise TypeError("Manager email should be a string.")

        valid_clinic_names = ['AHR1300', 'Addison', 'Archer Lemont', 'Aurora Westbrook', 'BT', 'BL', 'BR Village',
                              'Burbank', 'CG', 'Clay', 'DG Main St', 'Division', 'GE', 'GE 854', 'HS', 'Iroquois',
                              'Joliet', 'Lisle', 'Lockport', 'LOM', 'MMO NPV', 'Marketplace', 'New Lenox',
                              'North Creek', 'Oak Lawn', 'Orland Hills', 'Ogden', 'PASQ', 'RT 59', 'Rt 56 WTN',
                              'Saddlewood', 'SH', 'SW 102', 'WASH', 'WDG', 'WTN', 'Weber Rd', 'Westmont',
                              'Westmont Ogden', 'York']
        if clinic not in valid_clinic_names:
            raise TypeError("Clinic name should be a string.")

        if not isinstance(request_type, str):
            raise TypeError("Request type should be a string.")

        if not isinstance(start_time, datetime):
            raise TypeError("Start time should be of type datetime.datetime.")

        if not isinstance(end_time, datetime):
            raise TypeError("End time should be of type datetime.datetime.")

        if start_time > end_time:
            raise ValueError("Start time cannot be greater than End time.")

        if start_time.weekday() == 6 or end_time.weekday() == 6:
            raise ValueError("Start and End time should be on weekdays. All clinics are closed on Sundays.")

        start_time_hour = start_time.hour
        end_time_hour = end_time.hour
        if start_time_hour < 6 or start_time_hour >= 20 or end_time_hour < 6 or end_time_hour >= 20:
            raise ValueError("Start and End time should be between 6:00 am and 8:00 pm.")

        valid_request_types = ["Needs a Tech", "Has a Tech to Spare", "Needs to Relocate a Therapist",
                               "Can Accommodate a Therapist"]
        if request_type not in valid_request_types:
            raise ValueError("Invalid Request type. Valid types are: " + ", ".join(valid_request_types))

        if start_time.date() != end_time.date():
            raise ValueError("Start date and End date should be same.")

        self.manager = manager_name
        self.manager_email = manager_email
        self.clinic = clinic
        self.request_type = request_type
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"StaffingRequest({self.manager}, {self.manager_email}, {self.clinic}, {self.request_type}, {self.start_time}, {self.end_time})"

    def __repr__(self):
        return f"StaffingRequest({self.manager}, {self.manager_email}, {self.clinic}, {self.request_type}, {self.start_time}, {self.end_time})"
