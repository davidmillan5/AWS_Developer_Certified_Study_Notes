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


### Connecting to Other Networks

By default, an Amazon VPC is an isolated network. Instances within an Amazon VPC cannot communicate with the Internet or other networks until you explicitly create connections.


<p align="center">
  <img src="https://docs.aws.amazon.com/es_es/vpc/latest/userguide/images/how-it-works.png" alt="AWS Virtual Private Network">
</p>