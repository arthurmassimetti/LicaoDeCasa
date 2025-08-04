<img width="1089" height="660" alt="image" src="https://github.com/user-attachments/assets/05591556-e7f3-4a21-8d82-52275ac850d4" />

verificar o ecosystem 

```json
module.exports = {
  apps: [
    {
      name: "api",
      script: "./api/bin/www",
      cwd: "./api",
      watch: true,
      instances: 1,
      env: {
        NODE_ENV: "development"
      },
      env_production: {
        NODE_ENV: "production"
      }
    },
    {
      name: "extrator",
      script: "./extrator/bin/www",
      cwd: "./extrator",
      watch: true,
      instances: 1,
      env: {
        NODE_ENV: "development"
      },
      env_production: {
        NODE_ENV: "production"
      }
    }
  ]
};

```

Ver as rotas certas
