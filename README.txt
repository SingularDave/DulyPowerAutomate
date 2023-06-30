This API finds matching requests for staffing needs across different clinics and notifies the managers via email.

Power Automate will submit requests from the List by making a POST request to the /clinic-requests endpoint with a payload in the following format:

```json
{
  "body": [
    {
      "manager_name": "Jane Doe",
      "manager_email": "jane@clinic.com",
      "clinic": {"Value": "Addison"},
      "request_type": {"Value": "Needs a Tech"},
      "start_datetime": "2022-05-17T09:00:00Z",
      "end_datetime": "2022-05-17T17:00:00Z"
    },
    ...
  ]
}
```

The API will then:

1. Check if any of the requests overlap in time
2. Check if the clinics are nearby using a predefined dictionary
3. Check if the request types match using another dictionary
4. If a match is found, an email is generated and returned in the response with the managers' email addresses and email template. Power Automate will then send the email to the managers via Outlook.

For example:
```json
{
  "Matching requests": [
    {
      "manager_email": "jane@clinic.com",
      "last_manager_email": "john@clinic.com",
      "email_template": "<email template>"
    }
  ]
}
```

Otherwise, an empty list is returned.

The code contains input validation to ensure that only valid request objects are created.