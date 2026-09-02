# Task 3 — Deploying 3 different application types with Docker

Three small, self-contained apps, each with its own Dockerfile:

| App | Folder | Port |
|---|---|---|
| Node.js | `nodejs-app/` | 3000 |
| Python (Flask) | `python-app/` | 5000 |
| Java | `java-app/` | 8000 |

Run each block from inside its own folder.

## Node.js app

```bash
cd nodejs-app
docker build -t nodejs-app .
docker run -d --name nodejs-container -p 3000:3000 nodejs-app
curl http://localhost:3000
```

Expected: `Hello from the Node.js Docker app!`

![alt text](<Screenshot 2026-08-31 203209.png>)

## Python app

```bash
cd python-app
docker build -t python-app .
docker run -d --name python-container -p 5000:5000 python-app
curl http://localhost:5000
```

Expected: `Hello from the Python Docker app!`

![alt text](<Screenshot 2026-08-31 203705-1.png>)

## Java app

```bash
cd java-app
docker build -t java-app .
docker run -d --name java-container -p 8000:8000 java-app
curl http://localhost:8000
```

Expected: `Hello from the Java Docker app!`

![alt text](<Screenshot 2026-08-31 203808.png>)

## Verify all three are running together

```bash
docker ps
```

You should see `nodejs-container`, `python-container`, and `java-container`
all `Up`, each with its own port mapping. This is your key screenshot for
Task 3.

## Cleanup (optional)

```bash
docker stop nodejs-container python-container java-container
docker rm nodejs-container python-container java-container
```
