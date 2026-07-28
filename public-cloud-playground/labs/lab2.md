# Lab 2 — Store Files in Amazon S3

**Objective:** Create an S3 bucket and upload an object that's accessible over a public URL.

**Estimated time:** 20–25 minutes
**Region for this training: `eu-west-1` (Europe – Ireland) only.** Your trainer has raised the account service quotas specifically for `eu-west-1`; resources created in other regions may hit default limits and fail.
**Estimated cost:** Effectively free for this lab (a handful of small objects for a few minutes falls well within the S3 Free Tier / Always Free allowances). Cleanup is still required, since public buckets left running are a security risk, not just a cost one.

> **Shared account note:** everyone in this session is using the same AWS account under one shared login. S3 bucket names are globally unique across *all* AWS customers worldwide, not just within your account — so include your name and a random number in the bucket name (as shown below) to avoid a naming collision with another participant in the same session.

---

## Part 1: Create the Bucket

- [ ] In the search bar at the very top of the AWS Console, type `S3`.
- [ ] A dropdown appears below the search bar. Click **S3** (top result, under "Services").
- [ ] You land on the S3 console. In the **left-hand navigation menu**, confirm **General purpose buckets** is selected (it's usually the very first item, and the page defaults to it).
- [ ] The main panel shows a (possibly empty) table titled "Buckets" or "General purpose buckets", listing name, region, and creation date columns. In the **top-right** of that panel, click the orange **Create bucket** button.

### General configuration

- [ ] You're now on the "Create bucket" page. The first section is **General configuration**. Confirm the small toggle near the top shows **General purpose** selected (not "Directory" — that's a different, more advanced bucket type we don't need).
- [ ] Find the **Bucket name** field. Click into it and type a **globally unique** name: `<yourname>-cloud-lab-<random-number>` — for example, `sarah-cloud-lab-4471`. Use your real name, all lowercase, no spaces or underscores (dashes are fine). Bucket names are shared across *every* AWS customer in the world, so a plain name like `test-bucket` will almost certainly already be taken — the random number at the end avoids that.
- [ ] Below the bucket name, find **AWS Region** — click the dropdown and select **Europe (Ireland) eu-west-1**. Double-check this, since it's easy to accidentally leave it on whatever region the console last remembered.

### Object Ownership

- [ ] Scroll down to the **Object Ownership** section. You'll see two large radio-button options:
  - **ACLs disabled (recommended)** — described underneath as "Bucket owner enforced". This should already be selected by default.
  - "ACLs enabled" — a second, legacy option.
- [ ] Leave **ACLs disabled (recommended)** selected. We're deliberately not using the legacy ACL method in this lab — we'll grant public access with a bucket policy instead, a few steps from now.

### Block Public Access settings for this bucket

- [ ] Scroll down to **Block Public Access settings for this bucket**. You'll see a single checkbox labelled **Block all public access**, checked by default, with four greyed-out sub-items listed underneath it explaining exactly what it blocks.
- [ ] Click the **Block all public access** checkbox to **uncheck** it.
- [ ] The four sub-items below become individually editable, and a **yellow warning box** appears below them with text similar to: *"Turning off block all public access might result in this bucket and the objects within becoming public."*
- [ ] Inside that warning box, there's a checkbox labelled something like **"I acknowledge that the current settings might result in this bucket and the objects within becoming public."** — click it to check it. Without checking this box, the "Create bucket" button at the bottom of the page will refuse to work.

> ⚠️ This step is genuinely only appropriate for this short-lived training bucket. Never uncheck Block Public Access on a bucket holding anything real — customer data, credentials, business documents, and so on.

### The rest of the page

- [ ] Scroll past **Bucket Versioning** — leave it on **Disable** (the default).
- [ ] Scroll past **Default encryption** — leave it at its default setting (typically "Server-side encryption with Amazon S3 managed keys (SSE-S3)").
- [ ] Scroll past **Advanced settings (Object Lock)** — leave it on **Disable**.
- [ ] Scroll to the very bottom of the page and click the orange **Create bucket** button.
- [ ] You'll briefly see a loading indicator, then land back on the bucket list with a green success banner at the top reading something like *"Successfully created bucket '`<yourname>-cloud-lab-XXXX`'."* Your new bucket now appears as a row in the table.

---

## Part 2: Upload a File

- [ ] From the bucket list, click directly on your bucket's **name** (it's a blue clickable link, not just plain text) to open it.
- [ ] You land on the bucket's detail page, showing several tabs across the middle of the screen: **Objects**, **Properties**, **Permissions**, **Metrics**, and others. The **Objects** tab should already be selected — this is where uploaded files will appear.
- [ ] The Objects tab currently shows an empty table with a message like "You don't have objects in this bucket." In the **top-right** of this panel, click the orange **Upload** button.
- [ ] You're now on the "Upload" page. Click the **Add files** button (there's also a drag-and-drop area next to it, but we'll use the button).
- [ ] Your operating system's file picker dialog opens. Browse to and select a small, non-sensitive file on your own computer — a `.txt` file or a small image is ideal. **Never select anything containing personal, financial, or confidential data** — remember, you're about to make this bucket's contents public.
- [ ] Click **Open** (or your OS's equivalent) in the file picker. You'll return to the Upload page, and your chosen file now appears in a list under "Files and folders", along with its size.
- [ ] Scroll to the bottom of the page and click the orange **Upload** button.
- [ ] A new page appears showing upload progress, then a green banner reading **"Upload succeeded"** once complete, along with a summary showing 1 file uploaded.

> You'll notice there was no "make this file public" checkbox anywhere in that upload flow — that's expected and correct. Because ACLs are disabled on this bucket, public access can only be granted at the *bucket* level, which is exactly what the next part does.

- [ ] Click **Close** (top-right of this results page), or click your bucket's name in the breadcrumb trail near the top of the screen, to return to the bucket's Objects tab. Confirm your uploaded file now appears as a row in the table.

---

## Part 3: Grant Public Read Access via a Bucket Policy

- [ ] While still on your bucket's detail page, click the **Permissions** tab (in that same row of tabs as "Objects").
- [ ] Scroll down this page until you find the **Bucket policy** section (it's below "Block public access (bucket settings)" and "Access control list"). It currently shows no policy, with an **Edit** button in the top-right of that section. Click **Edit**.
- [ ] A large empty text box appears, titled "Policy", with a link below it to a "Policy generator" tool (we won't use that — we'll paste a ready-made policy directly).
- [ ] Click into the empty text box and paste the following exactly:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
    }
  ]
}
```

- [ ] **Before saving**, find `YOUR-BUCKET-NAME` inside the pasted text (it appears once, inside the `"Resource"` line near the bottom) and replace it with your actual bucket name — for example, `arn:aws:s3:::sarah-cloud-lab-4471/*`. Keep the `/*` at the very end exactly as-is; without it, the policy applies to the bucket itself rather than the files inside it, and AWS will reject the policy with an error.
- [ ] Scroll down and click the orange **Save changes** button at the bottom of the page.
- [ ] You'll return to the Permissions tab, and the Bucket policy section now displays your saved JSON. Scroll back up to the top of the page — you should also see a small orange **Public** label now appearing next to the bucket's access summary.

---

## Part 4: Verify the File Is Publicly Accessible

- [ ] Click back to the **Objects** tab.
- [ ] Click directly on your uploaded file's **name** (the blue link) in the table — this opens the object's own detail page, not a download.
- [ ] On this page, find the field labelled **Object URL** — it will look like `https://<yourname>-cloud-lab-4471.s3.eu-west-1.amazonaws.com/yourfilename.txt`. Click the small copy icon next to it to copy the full URL.
- [ ] Open a **new private/incognito browser window** (this matters — a normal browser tab might already have AWS console credentials cached, which could make a broken policy look like it's working when it isn't). Paste the URL and press Enter.
- [ ] Confirm the file loads directly in the browser — for a `.txt` file, you'll see its raw text content; for an image, the image itself. If you see this without being asked to log in anywhere, the bucket policy is working correctly.

---

## S3 Concepts Learned

- Buckets and objects
- Globally unique bucket naming
- Object URLs
- Object Ownership settings and why ACLs are now disabled by default
- Block Public Access, and why it's a bucket-level *and* account-level setting
- Bucket policies as the current recommended method for granting public access
- Storage classes (Standard, Standard-Infrequent Access, Glacier Instant Retrieval, Glacier Flexible Retrieval, Glacier Deep Archive)
- High durability through automatic multi-Availability-Zone replication
- Static website hosting (S3 can serve a bucket's contents directly as a website — a natural next step beyond this lab)

---

## S3 Best Practices

- Keep buckets private unless public access is genuinely required for the use case.
- Never upload sensitive or personal information into a bucket that is, or might become, public.
- Prefer bucket policies over ACLs for granting access — this is now AWS's own guidance, not just a style preference.
- Use lifecycle policies to automatically transition older objects to cheaper storage classes (or delete them) and reduce cost over time.
- Delete demo/lab buckets and objects promptly after use — a forgotten public bucket is a real-world source of data leaks.

---

## Troubleshooting

- **Object URL gives "Access Denied":** go back to the **Permissions** tab and confirm two things: (1) under **Block public access (bucket settings)**, click **Edit** and confirm "Block all public access" is unchecked, and (2) the **Bucket policy** section still shows your saved JSON with the correct bucket name in the `Resource` line. S3 enforces the *most restrictive* combination of account-level and bucket-level settings — if a trainer or admin has Block Public Access forced on at the account level, individual bucket settings can't override it; flag this to your trainer if it happens.
- **Bucket policy won't save / shows a red error banner:** the most common cause is a typo in the bucket name inside the `Resource` line, or a missing `/*` at the end of it. Re-check the JSON character-for-character against the block above.
- **"Add files" button does nothing / no file picker opens:** try a different browser, or check whether your browser is blocking pop-ups for the AWS console domain.
- **File uploaded but no "Public" label appears next to the bucket:** this label can take a moment to update after saving the policy — try navigating away to the bucket list and back, or simply proceed to Part 4 and test the actual URL, which is the real test regardless of what the label shows.
- **Any "Access Denied" or quota-style error while creating the bucket itself:** confirm the region selector still shows **Ireland** — quotas for this training were only raised in `eu-west-1`.

---

## Cleanup

- [ ] From your bucket's **Objects** tab, tick the checkbox next to your uploaded file (or the checkbox at the very top of the table to select everything).
- [ ] Click the **Delete** button that appears above the table.
- [ ] A confirmation page appears listing the object(s) to be deleted. Type **`permanently delete`** into the confirmation text box exactly as instructed on screen, then click the red **Delete objects** button.
- [ ] Navigate back to the main S3 bucket list (click **General purpose buckets** in the left-hand menu, or **Amazon S3** in the breadcrumb at the top).
- [ ] Tick the checkbox next to your bucket's row.
- [ ] Click the **Delete** button above the table.
- [ ] A confirmation page appears — type your exact bucket name into the text box provided to confirm (this is a safety check, not an error), then click the red **Delete bucket** button.
- [ ] Confirm the bucket no longer appears in your bucket list.