# Project Verify.me - Marco Boschetti
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/MarcoBosc/MarcoBosc-Portfolio/blob/main/Verify.me/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/MarcoBosc/MarcoBosc-Portfolio/blob/main/Verify.me/README.pt-br.md)

# Project Scope
This project aims to develop an application that allows users to submit identification documents, such as RG or driver's license, along with additional information like full name and a photo, for authenticity verification. The application will then process these documents and return a validation on whether the documents match the user's identity. This tool will be useful for various purposes, such as identity authentication in online transactions, age verification in purchasing apps, among others. The project will be developed on an AWS architecture, utilizing technologies such as Amazon Textract, Rekognition, API Gateway, and others. All services will be provisioned in the Northern Virginia AWS region (us-east-1).

### Project Features
- [x] Fields for submitting necessary data (Full name, ID/Driver's License, photo with the document).
- [x] Visual feedback for fraud detection.

## Technologies
[Amazon Textract](https://aws.amazon.com/pt/textract/) is an Amazon Web Services (AWS) service that utilizes Machine Learning technology to extract text and data from documents. It can identify and extract information from documents in various formats, such as PDFs, images, and even scanned documents, facilitating document processing automation.

[Amazon Rekognition](https://aws.amazon.com/pt/rekognition/), on the other hand, is an image and video analysis service that also uses Machine Learning. It allows for the identification of objects, people, text in images, and even facial emotions. This makes it possible to automate tasks such as face identification in photos, detection of inappropriate content in videos, and much more.


## Architecture

<p align="center" width="100%">
    <img width="60%" src="../imgs/Verify.me.png">
</p>

The project architecture works as follows:
- The user accesses the application through the URL of the public bucket containing the entire web application.
- Upon submitting an identity verification test, the application sends a "POST" request to the [API Gateway](https://aws.amazon.com/pt/api-gateway/) and awaits its response asynchronously through the [fetch()](https://developer.mozilla.org/en-US/docs/Web/API/fetch) method of JavaScript. This request contains all the items added by the user (ID/Driver's License, full name, and photo with the document).
- The API Gateway then triggers the [lambda](https://aws.amazon.com/pt/lambda/), which is responsible for invoking Amazon Textract and Rekognition to perform identity verification.
- At this point, the Lambda returns whether fraud has been detected or not, i.e., whether the submitted data belongs to the same person or not.
- The API Gateway returns the Lambda's response to the application.
- The application displays on the screen whether the user is committing a potential fraud or not.

## Methodology
The project infrastructure will be deployed in the cloud using [terraform](https://www.terraform.io), where the state of each of the AWS resources used will be stored in an S3 bucket called verify-me-infra-remote-state-bucket. These states will be used to store the tf.state of the resources, allowing us to deploy and destroy the infrastructure in seconds thanks to Terraform. We will also use [GitHub Actions](https://docs.github.com/pt/actions) to create CI/CD (Continuous Integration and Continuous Delivery) pipelines, which are fundamental practices to enhance software quality.
### Replicating the project
Firstly, you need to have an [IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) configured in your AWS account, with your AccessKey and SecretAccessKeys. For replicating the project, you can choose to use GitHub Actions or not.

### With GitHub Actions
- Create a repository on GitHub for the project.
- In the Settings tab, locate the "Secrets and variables" field in the sidebar menu.
- Click on Actions and configure your AWS credentials in the "New repository secret" button.
<p align="center" width="100%">
    <img width="60%" src="../imgs/configureCredentials.png">
</P>
- Your secret names should be AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY, and the secret should be your respective credentials.
- Upload the Verify.me directory to the repository, this will trigger the Terraform Deploy pipeline.
- In the Actions tab, you can monitor the pipeline status.
- Done! Now just access the link of your bucket with the app and test it normally.

To destroy the project, simply click to execute the Terraform Destroy pipeline, then Terraform will automatically destroy all the infrastructure created during the Terraform Deploy pipeline execution.

### Without GitHub Actions

With [terraform installed](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) on your machine, simply open the terminal, navigate to the Verify.me project directory, and type the following commands:
- Initialize Terraform in your local directory:
    ```
    terraform init
    ```

- (Optional) Validate if everything is correct with the configuration of the .tf files:
    ```
    terraform validate
    ```

- Create an execution plan of the infrastructure:
    ```
    terraform plan
    ```

- Execute all steps defined by Terraform plan, also creating the .tfstate file:
    ```
    terraform apply -auto-approve
    ```

- Done! Now just access the link of your bucket with the app and test it normally.

To destroy the project, simply execute the command:
    ```
    terraform destroy -auto-approve
    ```
This will automatically destroy all the infrastructure created during the execution of the "terraform apply -auto-approve" command.

