# Chapter 3 AWS Data Storage

Cloud Storage is a critical component of cloud computing. Much of the power of the cloud lies in running your compute as close as possible to your storage.

> Because no single data store is ideal for all workloads, you'll need to consider each individual workload or component within your system and choose a data store that is right for it.
>
> The **AWS Cloud** is a reliable, scalable, and secure location for your data, offering:  
> - Object Storage  
> - File Storage  
> - Block Storage  
> - Data Transfer Services  

<!-- line break above by leaving an empty line, or use an HTML <br> -->

<p align="center">
  <img src="https://d2908q01vomqb2.cloudfront.net/cb4e5208b4cd87268b208e49452ed6e89a68e0b8/2018/03/20/aws-storage-soutions.jpg" alt="The AWS Storage Portfolio">
</p>

---

## Storage Fundamentals

The AWS storage portfolio starts with a few core data services:
- **Block storage** → [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/)
- **File storage** → [Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/)
- **Object storage** → [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) and [Amazon Glacier](https://aws.amazon.com/glacier/)

<p align="center">
  <img src="https://cdcloudlogix.com/wp-content/uploads/2022/02/aws-objects-01-1024x411.png" alt="The AWS Storage Types">
</p>

---

## Data Dimensions

Before choosing storage options, it’s important to evaluate your data and how you use it. Understanding concepts like data **velocity**, **variety**, and **volume** will help you choose the best storage type.

> Think in terms of a storage mechanism suitable for each workload—not a single store for the entire system.

### ⚡ Velocity, 🧩 Variety, and 📦 Volume

- **⚡ Velocity**: The speed of data reads and writes, measured in RPS/WPS; can be real-time, near-real-time, periodic, or batch.
- **🧩 Variety**: The structure and format of data: structured, semi-structured, unstructured, or BLOB data.
- **📦 Volume**: The total amount of data; larger volumes allow for richer insights and more complete archives, balanced by storage cost.

> Metrics to evaluate storage include maximum capacity and cost (e.g., $/GB).

---

## ❄️ Storage Temperature

**Storage temperature** describes how frequently data is accessed, helping select the right storage class to balance performance and cost:

- 🔥 **Hot Storage**: Frequently accessed, low latency; e.g., S3 Standard, EBS, EFS Standard.
- 🌤️ **Warm Storage**: Accessed occasionally; lower cost, moderate latency; e.g., S3 Standard-IA.
- ❄️ **Cold Storage**: Rarely accessed; low cost, longer retrieval; e.g., S3 Glacier.
- 🧊 **Frozen Storage**: Archival data, almost never accessed; lowest cost, longest retrieval; e.g., S3 Glacier Deep Archive.

---

> ✅ *Choose the right storage temperature and data store for each workload to optimize performance and cost.*


## Data Value

Although we would like to extract useful information from all the data we collecrt, not all data is equally important to us. Some data must be preserved at all costs, and other data can easily regenerated as needed or even lost without significant impact on the business. Depending on the value of data, we may be more or less willing to invest in additional durability.

