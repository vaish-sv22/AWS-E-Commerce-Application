# AWS 3-Tier E-Commerce Application Deployment

## Project Overview

This project demonstrates the deployment of a **3-Tier E-Commerce Application on AWS Cloud** using a highly available and scalable architecture.

The application is divided into three layers:

- **Web Tier (Frontend)** - Apache HTTP Server running on EC2 instances
- **Application Tier (Backend)** - Python Flask application running on EC2 instances
- **Database Tier** - Database server for storing application data

The architecture uses multiple EC2 instances to provide scalability, reliability, and fault tolerance.

---

# Architecture

![AWS E-Commerce Architecture](https://raw.githubusercontent.com/vaish-sv22/AWS-E-Commerce-Application/main/aws-3-tier-E-Commerce-applicatoin-main/AWS%20E-Commerce.png)

---

# Technologies Used

- AWS EC2
- Amazon Linux
- Apache HTTP Server
- Python Flask
- MySQL Database
- Git & GitHub
- Linux Shell Commands
- Reverse Proxy
- Load Balancing
- Security Groups

---

# Project Repository

GitHub Repository:
https://github.com/vaish-sv22/AWS-E-Commerce-Application

Clone the project:
git clone https://github.com/vaish-sv22/AWS-E-Commerce-Application.git

---

# Frontend Deployment (Web Tier)

Frontend is deployed on **two EC2 instances** using Apache HTTP Server.

## Step 1: Update System Packages

sudo yum update -y

## Step 2: Install Apache HTTP Server

sudo yum install httpd -y

## Step 3: Start Apache Service

sudo systemctl restart httpd
sudo systemctl enable httpd

## Step 4: Install Git

sudo yum install git -y

## Step 5: Clone Repository

git clone https://github.com/vaish-sv22/AWS-E-Commerce-Application.git

## Step 6: Copy Frontend Files

sudo cp -r AWS-E-Commerce-Application/frontend/* /var/www/html/

## Step 7: Restart Apache

sudo systemctl restart httpd

Access the frontend application:
http://<frontend-public-ip>

---

# Apache Reverse Proxy Configuration

The frontend Apache server forwards API requests to backend Flask servers.

Create proxy configuration:
sudo vi /etc/httpd/conf.d/backend-proxy.conf


Add the following configuration:

apache
ProxyRequests Off
ProxyPreserveHost On

<Proxy "balancer://backendcluster">

BalancerMember "http://BACKEND_PRIVATE_IP_1:5000" route=server1

BalancerMember "http://BACKEND_PRIVATE_IP_2:5000" route=server2


ProxySet lbmethod=byrequests

</Proxy>


ProxyPass "/api/" "balancer://backendcluster/"

ProxyPassReverse "/api/" "balancer://backendcluster/"


ProxyPass "/static/" "balancer://backendcluster/static/"

ProxyPassReverse "/static/" "balancer://backendcluster/static/"


Replace:
BACKEND_PRIVATE_IP_1
BACKEND_PRIVATE_IP_2

with your backend EC2 private IP addresses.

Restart Apache:
sudo systemctl restart httpd

---

# Backend Deployment (Application Tier)

Backend Flask application is deployed on **two EC2 instances**.

## Step 1: Create Application Directory

sudo mkdir /products

## Step 2: Install Git

sudo yum install git -y

## Step 3: Clone Repository

git clone https://github.com/vaish-sv22/AWS-E-Commerce-Application.git

## Step 4: Copy Backend Files

sudo cp -r AWS-E-Commerce-Application/backend/* /products/

---

# Install Python Dependencies

Install Python pip:
sudo yum install python3-pip -y

Install required packages:
pip3 install -r /products/requirements.tx

---

# Run Flask Application

Start backend application:
python3 /products/app.py

Application runs on:
http://<backend-private-ip>:5000

Example:
Running on http://172.31.xx.xx:5000

---

# Test Backend API

Check application locally:
curl -s http://localhost:5000/products | jq

Test using backend private IP:
curl -s http://BACKEND_PRIVATE_IP:5000/products | jq

---

# Security Group Configuration

## Frontend EC2 Security Group

Allow HTTP traffic:

| Type | Port | Source |
|---|---|---|
| HTTP | 80 | 0.0.0.0/0 |

---

## Backend EC2 Security Group

Allow Flask application communication:

| Type | Port | Source |
|---|---|---|
| Custom TCP | 5000 | Frontend EC2 Private IP |

---

## Database Security Group

Allow database access:

| Type | Port | Source |
|---|---|---|
| MySQL | 3306 | Backend EC2 Security Group |

---

# Application Flow

1. User accesses the application through the Load Balancer.
2. Frontend EC2 instances serve HTML, CSS, and JavaScript files using Apache.
3. API requests are forwarded through Apache Reverse Proxy.
4. Backend Flask servers process application requests.
5. Backend communicates with the database.
6. Response is returned to the user.

---

# Future Enhancements

- Implement Auto Scaling Group
- Add Amazon RDS MySQL Database
- Add HTTPS using AWS Certificate Manager
- Add CI/CD Pipeline using GitHub Actions
- Add CloudWatch Monitoring
- Add Docker Containerization



