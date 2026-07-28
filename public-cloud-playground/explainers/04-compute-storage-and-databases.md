# Building Blocks: Compute, Storage & Databases
### EC2, S3, RDS, DynamoDB & Serverless

---

## Introduction

With Regions, Availability Zones, and the concept of a Service established, this document looks closely at the specific services most commonly used to actually build something in the cloud: virtual servers, storage, and databases — using AWS as the running example throughout, since the concepts transfer directly to every other provider. Two real stories run through this document: how a three-person team scaled a photo-sharing app to 14 million users on EC2, and how a database outage during Amazon's own busiest shopping week led directly to the creation of DynamoDB.

---

## 1. Running Servers — EC2, AMIs, and Instance Types

**EC2 (Elastic Compute Cloud)** is AWS's virtual server service. A running EC2 server is called an **instance**, launched from a template called an **AMI (Amazon Machine Image)**, using a chosen **instance type** — the size of the machine, in terms of CPU and memory.

**Real-world analogy — ordering a custom laptop online:** The **AMI** is the pre-installed software image (which operating system, which applications). The **instance type** is the spec sheet you choose (8GB RAM vs. 32GB RAM, 2 cores vs. 8 cores).

AMIs can come from several sources: standard Linux/Windows images provided by the platform itself, third-party images from a Marketplace, or images you build yourself.

```mermaid
graph TD
    AMI["📀 AMI<br/>(template: OS + software)"]:::ami -->|"launch"| INST["🖥️ EC2 Instance<br/>(running server)"]:::instance
    TYPE["📏 Instance Type<br/>(CPU/RAM size)"]:::type -->|"defines size of"| INST

    classDef ami fill:#D2B4DE,stroke:#7D3C98,stroke-width:2px,color:#4A235A
    classDef instance fill:#A3E4D7,stroke:#17A589,stroke-width:2px,color:#0B5345
    classDef type fill:#AED6F1,stroke:#2E86C1,stroke-width:2px,color:#154360
```

### Hard Drives — EBS

EC2 servers use **EBS (Elastic Block Store)** volumes for storage — virtual hard drives that behave much like physical ones. They can be magnetic or solid-state, provisioned with a minimum read/write speed, and — just like a physical drive — detached from one instance and reattached to a different one.

```mermaid
graph LR
    INST1["🖥️ EC2 Instance A"]:::instance -->|"attached to"| EBS["💾 EBS Volume<br/>(virtual hard drive)"]:::storage
    EBS -.->|"can be detached &<br/>reattached, like a<br/>physical drive"| INST2["🖥️ EC2 Instance B"]:::instance

    classDef instance fill:#A3E4D7,stroke:#17A589,stroke-width:2px,color:#0B5345
    classDef storage fill:#A9CCE3,stroke:#2874A6,stroke-width:2px,color:#1B4F72
```

### Real-World Story: Three Engineers, One Photo App, 14 Million Users

If EC2's pitch sounds abstract — "provision a server in minutes instead of weeks" — Instagram's early history is the sharpest possible illustration of what that actually enables.

<cite index="161-1">Instagram ran its infrastructure on Ubuntu Linux hosted on Amazon EC2 from the very beginning.</cite> <cite index="156-1">By December 2011, fourteen months after launch, Instagram had reached 14 million users — with a total engineering team of exactly three people.</cite> <cite index="156-2">By April 2012, Facebook acquired the company for $1 billion, at which point Instagram employed just 13 people in total.</cite> Instagram's own engineers were candid about *why* this was possible with such a small team: <cite index="161-2">with only three engineers and constantly evolving needs, building and running their own physical infrastructure was never seriously on the table.</cite>

```mermaid
graph LR
    Team["👥 3 Engineers"]:::team --> EC2["☁️ EC2 + Ubuntu<br/>(provisioned in minutes,<br/>not weeks)"]:::ec2
    EC2 --> Growth["📈 0 → 14 Million Users<br/>in 14 months"]:::growth

    classDef team fill:#D2B4DE,stroke:#7D3C98,stroke-width:2px,color:#4A235A
    classDef ec2 fill:#AED6F1,stroke:#2E86C1,stroke-width:2px,color:#154360
    classDef growth fill:#A3E4D7,stroke:#17A589,stroke-width:2px,color:#0B5345
```

This is Reason 4 from the very first document in this series ("speed and agility") made concrete: a team of three people, with no data centre, no hardware procurement process, and no facilities staff, scaled to 14 million users using instances and load balancers they configured themselves in a matter of minutes each. Building and racking physical servers for that same growth curve — on the timeline Instagram actually grew on — would simply not have been possible for a team that size.

---

## 2. Data Storage — Choosing the Right Tool for the Job

No single storage type suits every need — a technique often called **polyglot persistence**. A shopping cart needs millisecond-fast lookups; a finance report needs relational joins and transactions; a decade-old compliance record just needs to sit somewhere cheap and safe until it's needed. AWS alone offers several distinct storage services, each suited to a different job — including EBS (covered above), Instance Store (temporary SSD storage attached directly to an instance), ElastiCache (Memcached/Redis as a managed service), and the object storage and database services covered in detail below.

### S3 — Simple Storage Service

**S3** is a file storage service accessed over HTTP/S. Files are called **objects**, and objects are stored in **buckets**. It offers extraordinarily high durability — **99.999999999%** (informally, "eleven nines") — meaning the mathematical probability of ever losing a stored file is astronomically small, because S3 automatically and invisibly replicates every object across multiple facilities. (Azure's equivalent service is called Blob Storage.)

**Real-world analogy:** A safety deposit box service so obsessively redundant that even if the branch you used burned down, your box's contents already exist as verified copies at other branches you never even visited.

```mermaid
graph TD
    Bucket["🪣 S3 Bucket"]:::bucket --> Obj1["📄 Object"]:::object
    Bucket --> Obj2["📄 Object"]:::object
    Bucket --> Obj3["📄 Object"]:::object
    Obj1 -.->|"automatically replicated"| Multi["Multiple facilities,<br/>eleven-nines durability"]:::durable

    classDef bucket fill:#D2B4DE,stroke:#7D3C98,stroke-width:2px,color:#4A235A
    classDef object fill:#AED6F1,stroke:#2E86C1,stroke-width:2px,color:#154360
    classDef durable fill:#A3E4D7,stroke:#17A589,stroke-width:2px,color:#0B5345
```

---

## 3. Databases — RDS and DynamoDB

Two very different types of managed database service cover the majority of real-world needs:

### RDS — Relational Database Service

**RDS** is a managed relational database service, supporting engines like Oracle, SQL Server, MySQL, MariaDB, and PostgreSQL, with simple configuration of clusters and backups. AWS's own database, **Aurora**, is compatible with MySQL and PostgreSQL. (Azure's equivalent is called SQL Managed Instances.)

"Managed" is the key word here — the provider handles patching, backups, and failover clustering. You still write SQL and design your schema exactly as you would on a self-hosted database; you simply stop worrying about the server administration underneath it.

### DynamoDB — Managed NoSQL

**DynamoDB** is AWS's managed NoSQL database, built for extreme performance — single-digit millisecond latency at any scale — and very high availability (99.999%). Related services include DocumentDB ("MongoDB as a service") and Neptune (a graph database). (Azure's equivalent is called Cosmos DB.)

**Real-world analogy comparing the two:** RDS is a filing cabinet with neatly cross-referenced folders — powerful and flexible, but you need to know the filing system to search it well. DynamoDB is a wall of numbered lockers — if you know the locker number, retrieval is instant no matter how many lockers exist, but you can't easily "search across all lockers for anything starting with a G."

```mermaid
graph LR
    Q{"What does<br/>this data need?"}:::question
    Q -->|"Complex queries,<br/>relationships, transactions"| RDS["🗄️ RDS<br/>Relational database"]:::rds
    Q -->|"Extreme speed,<br/>simple key-based lookups"| DDB["⚡ DynamoDB<br/>NoSQL database"]:::dynamo

    classDef question fill:#FAD7A0,stroke:#B9770E,stroke-width:2px,color:#7E5109
    classDef rds fill:#AED6F1,stroke:#2E86C1,stroke-width:2px,color:#154360
    classDef dynamo fill:#A9CCE3,stroke:#2874A6,stroke-width:2px,color:#1B4F72
```

**A quick note on what "99.9%" vs. "99.999%" actually means:** 99.9% availability works out to roughly 8.7 hours of downtime per year; 99.999% availability works out to roughly 5 minutes per year. The extra "nines" represent a very real, very large difference in practice — and, as the story below shows, that difference was the entire reason DynamoDB was built in the first place.

### Real-World Story: The Outage That Invented a New Kind of Database

DynamoDB didn't start life as a product idea in a meeting room — it started as a fix for a very specific, very painful failure inside Amazon's own retail business.

<cite index="165-1">The story of DynamoDB began years before its 2012 launch, with a series of outages on Amazon's own e-commerce platform during the 2004 holiday shopping season.</cite> At the time, Amazon's shopping cart — the single most business-critical piece of the entire website — ran on a conventional relational database. <cite index="165-2">Given the volume of traffic during that 2004 holiday season, the relational database began experiencing hard-to-debug, hard-to-reproduce deadlocks under load.</cite> For an online retailer, this is close to the worst possible failure: a customer unable to complete a purchase because the shopping cart itself is unavailable is a lost sale, happening at the exact moment the business can least afford it.

Amazon's engineers realised the deeper problem wasn't a bug to be patched — it was a mismatch between what a relational database is designed to guarantee and what a shopping cart actually needs. A shopping cart doesn't need perfect, instantly-consistent data across every server in the world; it needs to **always be available**, even if that means briefly tolerating a duplicate item that gets cleaned up later. <cite index="164-1">In 2007, Amazon's CTO Werner Vogels and his team published their findings publicly in a paper titled "Dynamo: Amazon's Highly Available Key-Value Store," a paper widely credited with helping launch the entire NoSQL database market.</cite> <cite index="165-3">On January 18th, 2012, Amazon made this design available to every AWS customer as a fully managed service: DynamoDB, built for single-digit millisecond performance at any scale.</cite>

```mermaid
graph LR
    Event["🎄 2004 Holiday Season:<br/>Shopping cart deadlocks<br/>under peak load"]:::event --> Insight["💡 Insight: cart needs<br/>ALWAYS-available data,<br/>not perfect consistency"]:::insight --> Paper["📄 2007: Dynamo paper<br/>published (Vogels et al.)"]:::paper --> Product["🚀 2012: DynamoDB<br/>launched as a public service"]:::product

    classDef event fill:#F5B7B1,stroke:#C0392B,stroke-width:2px,color:#78281F
    classDef insight fill:#FAD7A0,stroke:#B9770E,stroke-width:2px,color:#7E5109
    classDef paper fill:#D2B4DE,stroke:#7D3C98,stroke-width:2px,color:#4A235A
    classDef product fill:#A3E4D7,stroke:#17A589,stroke-width:2px,color:#0B5345
```

This is a rare, well-documented case of a genuinely new category of technology tracing directly back to one specific, dated outage — and it's worth remembering the next time "99.999% availability" appears on a slide as just another number. For Amazon in December 2004, the gap between "the database is consistent" and "the database is available" was the gap between a completed sale and a lost customer.

---

## 4. Serverless — Removing the Server Entirely

**AWS Lambda** (or **Azure Functions**) removes the need to manage a server at all. You deploy a function, written in a language of your choice (Java, JavaScript, Python, C#, Go, Ruby), and the provider runs it only when something triggers it — a REST API call, a message, a file upload, a scheduled event, and more. You pay only for the time it actually executes; there's no cost for idle capacity.

**Real-world analogy:** EC2 is like employing a full-time chef, paid a salary whether customers walk in or not. Lambda is like a food-delivery gig worker who only gets paid — and only shows up — the moment an order comes in, and any number of them can show up simultaneously if 500 orders land at once.

```mermaid
graph LR
    T1["🌐 REST API call"]:::trigger --> L["λ Lambda Function"]:::lambda
    T2["📨 Message queue"]:::trigger --> L
    T3["📁 File upload"]:::trigger --> L
    T4["⏰ Scheduled event"]:::trigger --> L
    L --> Out["Runs code,<br/>then shuts down —<br/>pay only for execution time"]:::result

    classDef trigger fill:#AED6F1,stroke:#2E86C1,stroke-width:2px,color:#154360
    classDef lambda fill:#A9CCE3,stroke:#2874A6,stroke-width:2px,color:#1B4F72
    classDef result fill:#A3E4D7,stroke:#17A589,stroke-width:2px,color:#0B5345
```

Serverless functions are sometimes called **FaaS (Function as a Service)** — an even further-managed slice than PaaS, introduced in the previous document: you don't manage a server *or* a runtime, just the function code itself.

---

## 5. Bringing It All Together

| Concept | Real-World Analogy | Technical Meaning |
|---|---|---|
| EC2 Instance | A custom laptop you ordered | A running virtual server, launched from a template (AMI) |
| AMI | The pre-installed software image | The template used to launch an EC2 instance |
| EBS | A removable hard drive | Virtual block storage attached to an EC2 instance |
| S3 | An obsessively redundant safety deposit box | Object storage with eleven-nines durability |
| RDS | A filing cabinet with cross-referenced folders | A managed relational database |
| DynamoDB | A wall of numbered lockers | A managed NoSQL database, built for speed at scale |
| Lambda | A gig worker paid only per delivery | Serverless functions that run only when triggered |
| Instagram, 2010–2012 | 3 people, no data centre, 14 million customers | EC2's elasticity making a tiny team's scale possible |
| DynamoDB's origin, 2004–2012 | A shopping cart that must never say "unavailable" | Availability, not perfect consistency, driving a new database design |

**In summary:** EC2 provides virtual servers, launched from AMI templates and attached to EBS storage — and Instagram's own history shows just how far that elasticity can stretch a genuinely tiny team. For data that needs to be stored rather than computed, S3 offers extremely durable file (object) storage, while RDS and DynamoDB offer two very different flavours of managed database — relational and NoSQL — each suited to different needs. DynamoDB's own origin story, tracing back to a 2004 holiday-season database failure inside Amazon's own shopping cart, is a reminder that "availability" isn't an abstract marketing number; it was, quite literally, the lesson Amazon learned the hard way. And for workloads that don't need a server running continuously at all, Lambda removes the concept of a server entirely, running code only when something triggers it, and billing only for that execution time.

---

*Prepared as a technical reference document.*