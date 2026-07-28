# Watching for Trouble
### Auditing, Threat Detection & Protection Tools

---

## Introduction

Locking down accounts and configuring the shared responsibility model correctly (covered in the previous document) is only half the picture. The other half is **visibility** — being able to see exactly who did what, and being alerted automatically when something looks wrong. This document covers the tools cloud providers offer for exactly that: audit logging, AI-driven threat detection, web firewalls, and sensitive-data discovery.

---

## 1. Auditing — Seeing Who Did What, and When

Cloud providers log every user action automatically: **CloudTrail** on AWS, **Activity Log** on Azure. These record who did what, when, and from where (source IP) — permanently, if configured to keep that history.

**Real-world analogy:** Every console click, every API call, every "who deleted that server?" question has an answer, permanently logged with a timestamp, username, and source IP — assuming logging hasn't been disabled (which is itself a loggable, suspicious action in its own right).

```mermaid
graph LR
    Action["🖱️ Any action taken<br/>(console, CLI, or API)"]:::action --> Log["📝 Logged automatically:<br/>Who, What, When, Source IP"]:::log --> Store["💾 Stored permanently<br/>for audit trails"]:::store

    classDef action fill:#AED6F1,stroke:#2E86C1,stroke-width:2px,color:#154360
    classDef log fill:#A9CCE3,stroke:#2874A6,stroke-width:2px,color:#1B4F72
    classDef store fill:#A3E4D7,stroke:#17A589,stroke-width:2px,color:#0B5345
```

**Why this matters, told through a real incident:** a sacked IT contractor once used a former colleague's login to destroy roughly £500,000 of a former employer's AWS infrastructure — and was later jailed, in large part because the audit trail made it possible to establish exactly what happened and who did it. This is precisely why individual, named IAM users matter so much (see the previous document) — shared logins make an audit trail far less useful, because you can't tell which specific person actually took the action.

---

## 2. Advanced Threat Detection — Letting AI Watch the Logs

Rather than a human manually reading through thousands of log entries, cloud providers offer AI-driven services that continuously monitor account activity and flag anomalies automatically:

- **AWS GuardDuty**
- **Azure Advanced Threat Protection** (databases only)
- **Google Cloud Armor**

**Real-world analogy:** CloudTrail is the building's CCTV footage — it records everything, but someone has to actively watch it. GuardDuty is an AI security guard that watches all the footage simultaneously and taps you on the shoulder the moment something looks wrong, instead of you finding out three weeks later during a routine review.

```mermaid
graph TD
    Logs["📼 CloudTrail /<br/>Activity Logs<br/>(everything recorded)"]:::logs --> AI["🤖 AI Threat Detection<br/>(GuardDuty, etc.)"]:::ai
    AI --> Pattern1["Repeated failed logins<br/>from an unusual IP<br/>(brute-force attempt)"]:::alert
    AI --> Pattern2["Someone quietly disabling<br/>logging (covering tracks)"]:::alert

    classDef logs fill:#D5D8DC,stroke:#566573,stroke-width:2px,color:#212F3C
    classDef ai fill:#D2B4DE,stroke:#7D3C98,stroke-width:2px,color:#4A235A
    classDef alert fill:#F5B7B1,stroke:#C0392B,stroke-width:2px,color:#78281F
```

Two realistic, common patterns these tools catch: a brute-force login attempt against a server (many failed logins from an unusual location in a short time), and an attempt to cover tracks by quietly disabling logging itself — both recognisable, well-understood attack signatures rather than vague "AI magic."

---

## 3. Web Firewalls — Filtering Traffic Before It Ever Arrives

A **Web Application Firewall (WAF)** lets you write rules blocking malicious traffic to your web-facing resources, based on things like IP address, geographic location, known SQL-injection patterns, or specific URL patterns — and these rules can be managed across many accounts at once, or just within one.

**Real-world analogy:** A bouncer at a club door with a very specific rulebook — block anyone from a banned list (IP), block anyone from a location the venue doesn't serve (geolocation), and refuse entry to anyone trying to sneak in something dangerous disguised as something innocent (SQL injection / malicious payloads).

```mermaid
graph LR
    Traffic["🌐 Incoming Web Traffic"]:::traffic --> WAF["🛡️ Web Application Firewall"]:::waf
    WAF -->|"Blocked"| Bad1["Known-bad IP"]:::blocked
    WAF -->|"Blocked"| Bad2["Malicious pattern<br/>(e.g. SQL injection)"]:::blocked
    WAF -->|"Allowed"| Good["Legitimate request<br/>reaches your application"]:::allowed

    classDef traffic fill:#AED6F1,stroke:#2E86C1,stroke-width:2px,color:#154360
    classDef waf fill:#D2B4DE,stroke:#7D3C98,stroke-width:2px,color:#4A235A
    classDef blocked fill:#F5B7B1,stroke:#C0392B,stroke-width:2px,color:#78281F
    classDef allowed fill:#A3E4D7,stroke:#17A589,stroke-width:2px,color:#0B5345
```

---

## 4. Finding Sensitive Data Before It's a Problem

**Amazon Macie** automatically scans S3 storage to identify where personally identifiable information (PII) is being stored, provides insight into how that data is being accessed, and flags anything that's publicly visible. (There is currently no direct equivalent offered on Azure.)

**Why this matters:** sensitive data — national insurance numbers, card numbers, health records — has a habit of ending up in unexpected places, like a forgotten CSV export or a debug log. Macie continuously scans for these patterns and raises an alert before a compliance auditor — or an attacker — finds them first.

```mermaid
graph TD
    S3["🪣 S3 Storage"]:::s3 --> Macie["🔍 Amazon Macie<br/>scans continuously"]:::macie
    Macie --> Find1["Where is PII<br/>actually stored?"]:::finding
    Macie --> Find2["How is it<br/>being accessed?"]:::finding
    Macie --> Find3["⚠️ Is any of it<br/>publicly visible?"]:::warning

    classDef s3 fill:#AED6F1,stroke:#2E86C1,stroke-width:2px,color:#154360
    classDef macie fill:#D2B4DE,stroke:#7D3C98,stroke-width:2px,color:#4A235A
    classDef finding fill:#A3E4D7,stroke:#17A589,stroke-width:2px,color:#0B5345
    classDef warning fill:#F5B7B1,stroke:#C0392B,stroke-width:2px,color:#78281F
```

---

## 5. Where to Go for Best Practices

Each major provider publishes its own detailed security best-practice framework, worth bookmarking as ongoing reference rather than reading end to end in one sitting:

- **AWS** — the Well-Architected Framework's 5 Pillars
- **Azure** — the Security Best Practices and Patterns guide
- **Google Cloud** — the Security Foundations Guide

---

## 6. Bringing It All Together

| Concept | Real-World Analogy | Technical Meaning |
|---|---|---|
| CloudTrail / Activity Log | Building CCTV footage | Permanent log of every user action: who, what, when |
| GuardDuty / Threat Detection | An AI security guard watching all footage at once | Automated, AI-driven anomaly detection across account activity |
| Web Application Firewall | A bouncer with a specific rulebook | Rules blocking malicious traffic before it reaches your application |
| Amazon Macie | A specialist scanning for sensitive documents left in the open | Automated discovery of PII and public exposure risk in storage |

**In summary:** securing a cloud environment doesn't end at configuration — it requires ongoing visibility. Audit logs like CloudTrail record every action so nothing happens invisibly; AI-driven threat detection tools like GuardDuty watch those logs continuously so a human doesn't have to; web firewalls filter out malicious traffic before it ever reaches an application; and tools like Amazon Macie proactively hunt for sensitive data sitting somewhere it shouldn't be. Together with the account and infrastructure protections covered in the previous document, this completes the full picture of how cloud security actually works in practice — not as a single setting to switch on, but as a layered set of responsibilities and tools working together.

---

*Prepared as a technical reference document.*
