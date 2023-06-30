from fastapi import FastAPI
from pydantic import BaseModel, Field
from staffing_request import StaffingRequest
import datetime
from finding_matches import find_matching_requests
from email_matches import get_email_template

app = FastAPI()


# RequestItem class is used to parse the request body into a list of RequestItem objects
class RequestItem(BaseModel):
    manager_name: str = Field(..., alias="Manager Name")
    manager_email: str = Field(..., alias="Manager Email")
    clinic: dict = Field(..., alias="Clinic")
    request_type: dict = Field(..., alias="Request Type:")
    start_datetime: str = Field(..., alias="Start Date/Time:")
    end_datetime: str = Field(..., alias="End Date/Time")


class RequestPayload(BaseModel):
    body: list[RequestItem]


# Post request to /clinic-requests. Takes in a list of requests and returns a list of matching requests.
@app.post("/clinic-requests")
async def process_requests(request_payload: RequestPayload):
    staffing_requests = []
    for item in request_payload.body:
        manager_name = item.manager_name
        manager_email = item.manager_email
        clinic = item.clinic["Value"]
        request_type = item.request_type["Value"]
        start_datetime = datetime.datetime.fromisoformat(item.start_datetime.replace('Z', '+00:00'))
        end_datetime = datetime.datetime.fromisoformat(item.end_datetime.replace('Z', '+00:00'))
        staffing_request = StaffingRequest(manager_name, manager_email, clinic, request_type, start_datetime,
                                           end_datetime)
        staffing_requests.append(staffing_request)
    last_request = staffing_requests[-1]
    rest_of_requests = staffing_requests[:-1]
    matching_requests = find_matching_requests(last_request, rest_of_requests)
    if matching_requests:
        json_matching_requests = []
        for request in matching_requests:
            email_template = get_email_template(request, last_request)
            matching_manager_email = request.manager_email
            last_manager_email = last_request.manager_email
            json_matching_requests.append({
                "manager_email": matching_manager_email,
                "last_manager_email": last_manager_email,
                "email_template": email_template
            })
        return {"Matching requests": json_matching_requests}
    else:
        return {"Matching requests": []}
