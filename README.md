# REST-API-Serverless-Framework

###  Technologies:
 - Python
 - DDD
 - Clean Architecture
 - AWS
   - Access credentials have been provided
 - Serverless Framework
   - https://www.serverless.com/framework/docs
 - RESTAPI via FASTAPI
   - https://fastapi.tiangolo.com/
 
### Deliverables:
 - Source code in an archive (zip,7z,rar)
   - Includes all logic, scripts, deployment files
 - DB Design Access Patterns and Decision
   - Why did you create XX number of tables?
   - How will these be accessed?
 - Working and deployed RESTAPIs with Documentation
   - Should be accessible via the browser
   - Should be deployed in AWS

### Tasks:
 - Create a set of RESTAPIs that can be used to perform the following in AWS API Gateway:
   - Manage a Person with Basic Information (Retrieve, Create, Update, Delete)
     - First Name
     - Last Name
     - Preferred Name
     - Date of Birth
     - Gender
     - Marital Status
     - Mobile Number
     - Home E-mail
     - Office E-mail
     - Home Address
     - Office Address
   - REST API documentation must be created (refer to FastAPI)
   - All APIs created should integrate with another service.
     - Use the "auth" and "hub" api documentation from the references
     - Create, Update, and Delete APIs should integrate with the "auth service and hub service"
     - Retrieve APIs should have a retrieve single and retrieve all
       - These should retrieve from the "hub service" and not from your own database
 - Create a NoSQL database using AWS DynamoDB to store all the information
   captured via the RESTAPI
   - Use provisioned output of 1 only for both Read and Write
 - Use AWS Lambda for all python code and logic to be created
   - Must demonstrate DDD and Clean Architecture
   - Unit Testing for all logic
   - Error handling for all logic
 - Use “Serverless Framework” (https://www.serverless.com/framework/docs) for deploying all resources
   - Must deploy lambdas, api gateways, dynamodb, and other resources necessary

### Additional Guidelines
 - AWS Resources
   - All service names and resources should start with the word "integration" as part of its name.
   - All service names and resources should end with your name. example: “robert”
   - Use ap-southeast-1 as the AWS region
 - Sign-up as Practice Manager & Adviser using the following parameters:
   - autoConfirmUser: true
   - firstName: <Your First Name>
   - lastName: <Your Last Name>
   - email: <Your Email>
   - phoneNumber: <Your Mobile Number [Optional]>
   - practiceName: <{Your Name} TEST PRACTICE>
   - password: <Password>
   - groups: ["practice_manager", "adviser"]
   
### Directory Structure:
```tree
├── core
│   ├── (core logic)
├── usecase
│   ├── (directs communication between layers)
├── repository
│   ├── (translates between usecase and data_store)
├── controller
│   ├── (entry and exit points for the application)
├── external_gateway
│   ├── (all external communication)
├── data_store
│   ├── (Defines how data is stored)
```
