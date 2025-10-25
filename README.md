---

# 🐍 Flask Dockerized REST API

A minimal REST API built with Flask and containerized using Docker.
This project demonstrates how to build, run, and publish a Docker image for a Python-based web service.

---

## ✅ Features

* Simple Flask REST API (`/` endpoint)
* Fully Dockerized
* Easy local deployment
* Published on Docker Hub

---

## 📂 Project Structure

```
Flask-Dockerized-REST-API/
│
├── app.py
├── requirements.txt
└── Dockerfile
```

---

## 🚀 Run Locally (Without Docker)

```bash
pip install -r requirements.txt
python app.py
```

Visit: `http://127.0.0.1:5000`

---

## 🐳 Build Docker Image

```bash
docker build -t flask-api .
```

---

## ▶️ Run Container

```bash
docker run -p 5000:5000 flask-api
```

Visit: `http://127.0.0.1:5000`

---

## 📌 Tag Image (For Docker Hub)

```bash
docker tag flask-api samiaabid006/flask-api
```

---

## ⬆️ Push Image to Docker Hub

```bash
docker push samiaabid006/flask-api
```

---

## 📥 Pull Image (Anyone can use)

```bash
docker pull samiaabid006/flask-api
```

---

## 🧑‍💻 Author

**Samia Abid**

---

## 📜 License

This project is open-source and free to use.

---

If you want, I can:
✅ add screenshots
✅ include API examples
✅ add badges (Docker pulls, stars, etc.)
✅ improve formatting further

Just tell me!
