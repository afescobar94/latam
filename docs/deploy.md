# Project Deployment Documentation

## Deployment on AWS EC2

The project was deployed on Amazon Web Services (AWS) using an Elastic Compute Cloud (EC2) instance. The following steps and configurations were set up:

- **Instance Selection**: Leveraged the free trial option of EC2 for project deployment.
  
- **Elastic IP**: An Elastic IP was assigned to the EC2 instance to ensure a static public IP address. This aids in consistent access without the need to update the IP address in case the instance is stopped and restarted.
  
- **Security Group Configuration**: Security groups were configured to allow incoming traffic on specific ports from any IP address, ensuring that the application is accessible from anywhere.


## Continuous Integration and Continuous Deployment (CI/CD)

The project implements CI/CD using GitHub:

### Continuous Integration (CI):

- **Trigger**: CI processes are initiated every time there's a push to the `main` branch.

- **Test Execution**: For demonstration purposes, a basic test command is set up. It uses an echo statement, simulating the test passage:
  ```bash
  echo "Tests passed successfully!"

Continuous Deployment (CD):
Condition: CD starts only if the CI process completes successfully without any errors.

Deployment Steps: Once the CI confirms that tests pass (or in this case, the echo statement runs successfully), the CD process initiates the deployment to the AWS EC2 instance.

