locals {
  # Machine readable project name (lower case letters, dashes, and underscores)
  # This will be used in names of AWS resources
  project_name = "platform-flask"

  # Project owner (e.g. navapbc). Used for tagging infra resources.
  owner = "platform-admins"

  # URL of project source code repository
  code_repository_url = "https://github.com/navapbc/platform-test-flask"

  # Default AWS region for project (e.g. us-east-1, us-east-2, us-west-1).
  # This is dependent on where your project is located (if regional)
  # otherwise us-east-1 is a good default
  default_region = "us-east-1"

  github_actions_role_name = "${local.project_name}-github-actions"
}
