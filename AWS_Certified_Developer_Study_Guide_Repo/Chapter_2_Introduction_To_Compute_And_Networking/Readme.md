# Chapter 2: Introduction to Compute and Networking

AWS provides a broad set of compute options through the following services:

- Amazon Elastic Compute Cloud (Amazon EC2)
- Amazon Lightsail
- AWS Elastic Beanstalk
- Amazon Elastic Container Service (ECS)
- Amazon Elastic Container Service for Kubernetes (EKS)
- AWS Lambda
- VMWare Cloud
- Amazon App Runner

![AWS Compute](https://jayendrapatil.com/wp-content/uploads/2017/02/aws-compute-services.png)

---

## Amazon Elastic Compute Cloud

**Amazon Elastic Compute Cloud (EC2)** enables you to provision computing environments called **instances**.  
With Amazon EC2, you have the flexibility to choose the hardware resources you need.  
You are in control of the operating system and any other software that will run on the instance.

<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThp1zFRauqIx4DJ8rBx2G-CmTanziIsb7APg&s" alt="Amazon EC2">
</p>

---

## Instance Types

An instance will have a certain number of virtual CPUs (vCPUs) and a specific amount of RAM.  
___Instance types___ are rated for a certain level of **network throughput**.

<p align="center">
  <img src="https://www.eginnovations.com/blog/wp-content/uploads/2021/09/aws-ec2-instance-selection.jpg" alt="Amazon EC2 Instances">
</p>

<p align="center">
  <img src="https://www.nakivo.com/blog/wp-content/uploads/2022/03/The-naming-principle-of-AWS-EC2-instance-types-1.png" alt="Amazon EC2 Instances naming">
</p>

---

## Storage

Your instance requires **storage volumes** for both the root volume and any additional storage volumes that you want to configure.  
You can create persistent storage volumes with ___*Amazon Elastic Block Store (Amazon EBS)*___ to provide **block storage** devices for Amazon EC2 instances.

<p align="center">
  <img src="https://cdn.prod.website-files.com/63403546259748be2de2e194/6510ab90d75705217fe92a97_Img1b_Short2.gif" alt="AWS EBS">
</p>

> You attach an EBS  volume to a single instance at a time, but yoy may detach and reattach to instances at your discretion.

---

>certain EC2 instances typer are designated ***"EBS-optimized"***, meaning that they are tuned with enhanced network capabilities to achieve low latency when using EBS.


## Software Images

When an EC2 instance first boots, it requires an ***operating system (OS)*** and the configuration of attached storage volumes. an **Amazon Machine Image (AMI)** provides the template for the OS and applications on the root volume of your instance. AMIs also provide a block device mapping that can specify addtitional volumes to mount when an instance launches.

<p align="center">
  <img src="https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/images/ami_copy.png" alt="AWS AMI">
</p>


> AWS provides a variety of AMIs on different operating systems, some preconfigured with popular software packages.

## Network Interfaces

***Virtual Network Interfaces*** called ***Elastic Network Interfaces (ENIs)*** provide networking for your EC2 instances. Each instance is assigned a _primary network interface_ associated with a subnet of a VPC and receives a private IP address to communicate with other resoruces.

> To give your instance a public IP, you may allocate an **_Elastic IP_** to associate with the machine.

### Security Groups

Protect traffic entering and exiting an instance's network interface. **Security Groups** act as a _stateful_ firewall. To make network connections to your instance, you must set security group rules allow the connection.

## Accessing Instances

By default, Linux Amazon EC2 instances provide remote access through Secure Shell(SHH), and Windows Amazon EC2 instances provide remote access thropugh the Remote desktop Protocol (RDP). To connect to the services, you muts have the appropiate inbound rule on the security group for the instance.

- Amazon EC2 Key Pairs.
- Session Manager.
- EC2 Instance Connect.


## Instance Life Cycle

An ***Amazon EC2*** instance has three primary states: running, stopped and terminated.


<p align="center">
  <img src="https://jayendrapatil.com/wp-content/uploads/2020/06/ec2_instance_lifecycle.png" alt="EC2 Lifecycle">
</p>


### Obtaining AWS Credentials

usually when interacting with AWS services via the CLI or various programming language SDKs like boto, you must either explictly provide AWS credentials in the form of an access key ID and secret access key, or ensure that those values are set in environment variables.

> Instance profiles are how you assign an IAM role (with its associated policies) to an instance.

>A role can be used on many instance at once, but an instance can only have one role at a time. To update the permissions on an instance, you can either update the policies attached to its role or swap the attached role at any time.

## Amazon Virtual Private Cloud

***Amazon Virtual Private Cloud (VPC)*** provides isolated networks within your AWS account.


<p align="center">
  <img src="https://sdmntprwestus.oaiusercontent.com/files/00000000-16bc-6230-93b4-f4f7af02f0bf/raw?se=2025-07-23T23%3A53%3A08Z&sp=r&sv=2024-08-04&sr=b&scid=0f09b600-c6a8-52ae-a1ea-559bd4f42eb4&skoid=c156db82-7a33-468f-9cdd-06af263ceec8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-07-23T20%3A08%3A57Z&ske=2025-07-24T20%3A08%3A57Z&sks=b&skv=2024-08-04&sig=YxFNOZmA/TcQKrhHw1x2XTML8bLvvHoUrJ6vGaFP0io%3D" alt="AWS VPC Connections Types">
</p>



### Connecting to Other Networks

By default, an Amazon VPC is an isolated network. Instances within an Amazon VPC cannot communicate with the Internet or other networks until you explicitly create connections.


<p align="center">
  <img src="https://docs.aws.amazon.com/es_es/vpc/latest/userguide/images/how-it-works.png" alt="AWS Virtual Private Network">
</p>


## IP Addresses

When working with ***Amazon VPC***, all instances placed within a particular VPC are assigned one or more IP Addresses.

<p align="center">
  <img src="https://media.geeksforgeeks.org/wp-content/uploads/20241217170153436945/IPv4-address-format.webp" alt="IP Address Example">
</p>


## Private IP Addresses

**Private IP** addresses are ***IPv4*** addresses that are not reachable from internet.


<p align="center">
  <img src="https://media.amazonwebservices.com/blog/eip_m1_small_1.png" alt="IP Address Example">
</p>


## Public IP Addresses

Each ***EC2 instance*** is assigned a public IP address automatically, in addition to the private IP address.

> AWS managesthe association between an instance and a public **IPv4** address, and the association persists only while the instance is ***running***. You cannot manually associate or disassociate public IP addresses from instance. All public **IPv4** addresses come with a small hourly charge.

## Subnets

Within an Amazon VPC, you define one or more subnets. A subnet is associated with a specific availability zone within the region containing the VPC. Each subnet has its own block of private IP addresses defined using CIDR notation. This block is a subset of the overall IP address range assigned to the VPC and does not overlap with any other subnet in the same VPC.


<p align="center">
  <img src="https://aws-ia.github.io/cfn-ps-aws-vpc/docs/deployment_guide/images/vpc-architecture_diagram.png" alt="VPC architecture">
</p>


## Route Tables

Network traffic exiting a subnet is controlled with routes defined in a route table. A route is composed of two parts: a destination and a target for the network traffic.


<p align="center">
  <img src="https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2020/03/19/Slide1.png" alt="Route Tables">
</p>


## Security Groups


Security Groups in AWS act as virtual firewalls for your EC2 instances, controlling inbound and outbound traffic.
They allow or deny traffic based on defined rules for specific ports, protocols, and IP ranges.
Security groups are stateful, meaning if you allow incoming traffic, the response is automatically allowed out.


<p align="center">
  <img src="https://docs.aws.amazon.com/images/vpc/latest/userguide/images/security-group-details.png" alt="Security Groups">
</p>


## Network Access Control Lists

***Network Access Control Lists (NACLs)*** act as optional layer of security for your VPC subnets.
They control inbound and outbound traffic at the subnet level using numbered rules.
NACLs are stateless, so responses to allowed inbound traffic must also be explicitly allowed outbound.


<p align="center">
  <img src="https://www.form3.tech/_prismic-media/85a6a55544130d32fd88cca9cf62d2ba2f414cd511e34f9fc6bddd74620a600b.png?auto=compress,format" alt="Network Access Control Lists">
</p>



<p align="center">
  <img src="https://cloudiofy.com/wp-content/uploads/2022/07/default-nacl-rules.png" alt="Network Access Control Lists Rules Table">
</p>



### Network Address Translation 


***Network Address Translation (NAT)*** in AWS lets private subnet instances access the internet securely.
It translates private IP addresses to a public IP for outbound traffic while blocking unsolicited inbound connections.
You can use a NAT Gateway (managed, scalable) or a NAT instance (customizable) to implement it.


<p align="center">
  <img src="https://docs.aws.amazon.com/images/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/decentralized-ha-nat-gateway.png" alt="Network Address Translation">
</p>


### Monitoring Amazon VPC Network Traffic

Amazon VPC Flow Logs capture information about the IP traffic going to and from network interfaces in your VPC.
They help with troubleshooting, security analysis, and compliance monitoring.
Flow log data can be published to Amazon CloudWatch Logs or S3 for storage and analysis.


<p align="center">
  <img src="https://signoz.io/img/guides/2024/07/vpc-flow-logs-aws.webp" alt="VPC Flow Logs">
</p>






