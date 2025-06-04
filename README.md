## Creation process

```shell
fly launch # remember to add a postgres database
fly secrets set DB_CONNECTION_STRING={} # paste the connection string
```
Fly launch will create:
- A fly.toml
- A dockerignore
- A dockerfile

fly secrets set:
- Creates a secret named DB_CONNECTION_STRING
- Becase we execute the command on the directory where our application's fly.toml is, then this secret is bound to this application
- If you want to create secrets for another application you need to specify the application
```shell
fly secrets set DB_CONNECTION_STRING={} --app {another_app_name}
```

## Deployments after changes
```shell
fly deploy
```

## Connection to database
You can use to execute SQL in the PSQL console
```shell
fly postgres connect --app {postgres-app-name}
```

If you want to connect via IDE, port forward the database to your localhost
```shell
fly proxy 5432 -a {postgres-app-name}
```
As long as this process is active you can connect via your IDE (datagrip, dbeaver, pycharm...)