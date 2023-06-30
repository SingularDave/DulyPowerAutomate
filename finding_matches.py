from staffing_request import StaffingRequest
from typing import List
from matching_criteria import nearby_clinics_dict, matching_requests_dict


def do_shifts_overlap(request_1: StaffingRequest, request_2: StaffingRequest) -> bool:
    start_time_1 = request_1.start_time
    print(f"start_time_1: {start_time_1}")
    end_time_1 = request_1.end_time
    print(f"end_time_1: {end_time_1}")
    start_time_2 = request_2.start_time
    print(f"start_time_2: {start_time_2}")
    end_time_2 = request_2.end_time
    print(f"end_time_2: {end_time_2}")

    # Check if shifts overlap
    overlap = start_time_1 < end_time_2 and start_time_2 > end_time_1
    print(f"start_time_1 < end_time_2: {start_time_1 < end_time_2}")
    print(f"start_time_2 < end_time_1: {start_time_2 > end_time_1}")
    print(f"Overlap: {overlap}")
    return overlap


def are_requests_matching(request_1: StaffingRequest, request_2: StaffingRequest) -> bool:
    # Get the request types of the two StaffingRequest instances
    request_type_1 = request_1.request_type
    request_type_2 = request_2.request_type

    # Check if the request types have matching request types in the dictionary
    if matching_requests_dict[request_type_1] == request_type_2:
        print("are_requests_matching: True")
        return True

    print("are_requests_matching: False")
    return False


def are_locations_nearby(request_1: StaffingRequest, request_2: StaffingRequest) -> bool:
    # Get the clinic names from the StaffingRequest instances
    clinic_1 = request_1.clinic
    clinic_2 = request_2.clinic

    # Check if clinic_1 is a value for clinic_2 and vice versa in the dictionary
    if clinic_1 in nearby_clinics_dict.get(clinic_2, []):
        if clinic_2 in nearby_clinics_dict.get(clinic_1, []):
            print(f"are_locations_nearby: True")
            return True

    print(f"are_locations_nearby: False")
    return False


def find_matching_requests(single_request: StaffingRequest, request_array: List[StaffingRequest]) -> \
        List[StaffingRequest]:
    matching_requests_list = []

    for req in request_array:
        print(f"Checking if {single_request} matches {req}")
        if (do_shifts_overlap(single_request, req) and
                are_requests_matching(single_request, req) and
                are_locations_nearby(single_request, req)):
            matching_requests_list.append(req)

    return matching_requests_list
