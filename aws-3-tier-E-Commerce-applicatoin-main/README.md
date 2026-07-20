# aws-3-tier-E-Commerce-applicatoin

## Frontend (Web Tier) - do in on both 2 instances. 
=============
### update yum repo

yum update
### Install httpd using yum command
yum install httpd -y 

### Start httpd using systemctl command
systemctl restart httpd

### Install git using yum 
yum install git -y 
### git clone the code repository 
git clone https://github.com/cloudinstitution/aws-3-tier-E-Commerce-applicatoin.git
## copy the files under /var/www/html/ 
cp -r aws-3-tier-E-Commerce-applicatoin/frontend/* /var/www/html/

## Access you forntend application using your public ip
http://public-ip/

### Add proxy in apache instance  (Change 172.31.37.47 with the app-private instnce private-ip)

sudo tee /etc/httpd/conf.d/backend-proxy.conf > /dev/null <<'EOF'
ProxyRequests Off
ProxyPreserveHost On

<Proxy "balancer://backendcluster">

    BalancerMember "http://10.0.0.153:5000" route=server1
    BalancerMember "http://10.0.0.196:5000" route=server2

    ProxySet lbmethod=byrequests

</Proxy>

ProxyPass        "/api/"    "balancer://backendcluster/"
ProxyPassReverse "/api/"    "balancer://backendcluster/"

ProxyPass        "/static/" "balancer://backendcluster/static/"
ProxyPassReverse "/static/" "balancer://backendcluster/static/"

EOF


### Start httpd using systemctl command
systemctl restart httpd

## Backend (App Tier)
=====================
### create a application folder
mkdir /products

### Install httpd using yum command
yum install git -y
### git clone the code repository 
git clone https://github.com/cloudinstitution/aws-3-tier-E-Commerce-applicatoin.git
### copy application files inside the /products
cp -r aws-3-tier-E-Commerce-applicatoin/backend/* /products/

### Install python3-pip 
sudo yum install python3-pip -y
 
### pip3 install -r requirements
pip3 install -r /products/requirements.txt

### Run python3 app 
python3 /products/app.py

## App output ( check if you see with your instance private ip and replace your proviate ip) 
 * Running on http://172.31.45.105:5000 

## check if you applicatoin work locally. (Try it in another window)
curl -s http://localhost:5000/products | jq
## check if you applicatoin work locally. (Replace your private ip now)

curl -s http://172.31.45.105:5000/products | jq

## Enable security group with the port number 5000 from the public instance private ip.

