<h1 align="center">☁️ Secure Flask Microservice – Cloud & OpenStack Deployment</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-3.0-green?logo=flask" />
  <img src="https://img.shields.io/badge/Docker-Enabled-blue?logo=docker" />
  <img src="https://img.shields.io/badge/OpenStack-Ready-red?logo=openstack" />
  <img src="https://img.shields.io/badge/Cloud%20Computing-DevOps-lightgrey?logo=cloudflare" />
</p>

---

## 🌍 Project Overview

This project demonstrates the **deployment of a secure Flask web microservice** using **Docker** and **Docker Compose**, designed for integration into **private cloud infrastructures (OpenStack)**.

The goal is to simulate a **real-world DevOps & Cloud Engineering environment**, combining development, deployment, and basic supervision.

---

## 🎯 Objectives

- Build a lightweight **REST API** using Flask  
- Containerize the service with **Docker**  
- Deploy and run it via **Docker Compose**  
- Ensure security (non-root user, exposed ports, environment variables)  
- Prepare it for **cloud or OpenStack deployment**

---

## ⚙️ Features

- 🧩 Simple, modular microservice design  
- 🐳 Docker & Docker Compose setup  
- 🔐 Non-root execution inside containers  
- ☁️ OpenStack-ready for private cloud testing  
- 🩺 Health-check and ping endpoints for system supervision  

---

## 🧠 How to Run Locally

Run the following command inside your project folder:

```bash
docker compose up --build -d
