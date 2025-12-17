Docker Compose
```
services:
  confluence:
    container_name: confluence
    build: https://github.com/Tim-oxa/Confluence.git
    restart: always
    ports:
      - "127.0.0.1:6000:8000"
```
