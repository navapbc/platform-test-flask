environment_name = "dev"
tfstate_bucket   = "platform-flask-806908981117-us-east-1-tf"
tfstate_key      = "infra/app/service/dev.tfstate"
region           = "us-east-1"
db_vars = {
  access_policy_arn = "arn:aws:iam::806908981117:policy/app-dev-db-access"
  security_group_id = "sg-0ad10b6eaa7d9adfe"
  connection_info = {
    host        = "app-dev.cluster-czmrvcsezdkn.us-east-1.rds.amazonaws.com"
    port        = "5432"
    user        = "app"
    db_name     = "app"
    schema_name = "app"
  }
}
