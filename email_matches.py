import datetime


def format_datetime(dt):
    return dt.strftime("%m/%d/%y at %I:%M%p")


# Email template informing managers of a match
def get_email_template(request1, request2):
    email_template = f"""Subject: Staffing Request Match Found

Dear {request1.manager} and {request2.manager},

We have identified a potential match for your staffing requests.

{request1.manager}'s request:
Clinic: {request1.clinic}
Request Type: {request1.request_type}
Time: {format_datetime(request1.start_time)} until {format_datetime(request1.end_time)}

{request2.manager}'s request:
Clinic: {request2.clinic}
Request Type: {request2.request_type}
Time: {format_datetime(request2.start_time)} until {format_datetime(request2.end_time)}

We kindly ask you to review the details above and reply to this email thread to discuss and decide if you would like to pursue the staffing change. Please keep in mind that this is a time-sensitive matter, and prompt communication will help ensure favorable staffing.

Best regards,
Duly Staffing Flow"""
    print(email_template)
    return email_template

