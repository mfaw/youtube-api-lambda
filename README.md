# **YouTube API Lambda Deployment 🚀**  
Easily deploy a Python function to AWS Lambda that retrieves YouTube channel information using the YouTube API—without ever opening the AWS Console! This project simplifies the deployment process using **Terraform** and **Lambda Layers** to manage dependencies like the `requests` package.

YouTube video link: 

## **Overview**  
This repository contains everything you need to:
- Fetch **YouTube channel information** by **channel name** using the YouTube Data API.  
- Deploy the code on **AWS Lambda** with Python.  
- Use **Lambda Layers** to include external dependencies (like the `requests` package).  
- Expose the Lambda function as a **public HTTP endpoint** (no API Gateway required).


## **Features**  
- **Python Code**: A Lambda function that calls the YouTube API and returns channel details.  
- **Terraform Scripts**: Automate your infrastructure setup, including Lambda creation and layer management.  
- **Serverless Setup**: No server management needed, thanks to AWS Lambda.  
- **Public HTTP Endpoint**: Call your Lambda function directly from a browser or API client.


## **Prerequisites**  
Make sure you have the following installed:  
- [Terraform](https://www.terraform.io/downloads)  
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) (configured with credentials)  
- Python 3.x  
- YouTube Data API Key (Get it [here](https://console.developers.google.com/))

## **Contact**  
For any questions or suggestions, feel free to reach out via GitHub or the comments section of my YouTube tutorial!
