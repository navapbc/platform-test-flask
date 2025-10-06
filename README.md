# platform-test-flask

> **⚠️ This repository is archived.**
>
> The Flask application has been migrated to the [platform-test](https://github.com/navapbc/platform-test) repository as `app-flask`. All future development and updates will occur in that repository.
>
> This consolidation allows us to test multiple applications within a single infrastructure setup, better reflecting real-world platform usage.

This project was used to test the integration of [template-infra](https://github.com/navapbc/template-infra) and [template-application-flask](https://github.com/navapbc/template-application-flask).

## Environment URLs

* [Dev environment](http://app-dev-828855199.us-east-1.elb.amazonaws.com/docs)

## Dev environment credentials

* To get the API key for the dev environment (to use in Swagger docs), run the following command

    ```bash
    aws ssm get-parameter --name "/app-dev/api-auth-token" --with-decryption --query Parameter.Value --output text
    ```
