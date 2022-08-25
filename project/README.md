# Software Quality Assurance Project
### Objective
This project requires us to create a CI/CD pipeline using ```Jenkins``` for any development project.
### Implementation
- Install ```Jenkins``` and start it (default localhost:8080)
- Signup on ```Ngrok``` to access ```localhost:8080``` using assigned link
- Create ```git-webhook``` and add ngrok url to the payload url in webhook
- Setup the webhook to trigger on new push
- Commit and push to the Git Repository which will trigger the first build
- Create ```jenkins-pipeline``` by adding build steps in the configure setting
