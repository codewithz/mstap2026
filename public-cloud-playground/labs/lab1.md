# Lab 1 — Launch an EC2 Server and Connect via SSH

**Objective:** Launch a virtual machine on Amazon EC2, connect to it securely using an SSH key pair, and install a simple web server by hand — the foundational skills every later lab in this course builds on.

**Estimated time:** 30–40 minutes
**Region for this training: `eu-west-1` (Europe – Ireland) only.** Service quotas (VPCs, vCPUs, Elastic IPs, etc.) are set per region, and your trainer has raised the limits needed for this course specifically in `eu-west-1`. If you create resources in any other region, you will hit default AWS account limits and the action will fail with a quota/limit error.

> **Shared account note:** everyone in this session is using the same AWS account under one shared login. To keep resources identifiable — and cleanup straightforward — **every resource you create in this lab must include your name**, exactly as shown in each step below (e.g. `<yourname>-server`, `<yourname>-web-sg`, `<yourname>-keypair`). Don't accept AWS's auto-generated default names.

---

## Before You Start: Confirm Your Region

This matters enough to do first, on its own, before anything else.

- [ ] Look at the very top-right corner of the AWS Console browser window, next to your account name. You'll see a region name displayed there (e.g. "N. Virginia" or "Ireland") with a small down-arrow next to it.
- [ ] Click that region name. A dropdown list of all AWS regions appears, grouped by geography (e.g. "US East", "Europe", "Asia Pacific").
- [ ] Under the **Europe** group, find and click **Europe (Ireland) eu-west-1**.
- [ ] The page will refresh. Confirm the top-right corner now reads **Ireland**. If it doesn't, repeat this step before continuing — every step below assumes you're in this region.

---

## Part 1: Create a Key Pair

A key pair is how you'll prove your identity to the server later, instead of using a password.

- [ ] In the search bar at the very top of the AWS Console (it has a magnifying glass icon and the placeholder text "Search"), type `EC2`.
- [ ] A dropdown appears below the search bar showing matching services. Click **EC2** (it will be the top result, under the "Services" heading).
- [ ] You're now on the EC2 dashboard. On the **left-hand side** of the screen, you'll see a navigation menu with several collapsible sections: "Instances", "Images", "Elastic Block Store", "Network & Security", "Load Balancing", and others.
- [ ] Click **Network & Security** to expand that section if it isn't already expanded (a small arrow next to it will point downward when expanded).
- [ ] Under **Network & Security**, click **Key Pairs**.
- [ ] You'll land on a page titled "Key Pairs" with a (likely empty) table and an orange button in the top-right of that table area labelled **Create key pair**. Click it.
- [ ] A panel opens on the right-hand side of the screen (or a full page, depending on your browser width) with the following fields, top to bottom:
  - [ ] **Name** — click into this text box and type: `<yourname>-keypair` (replace `<yourname>` with your actual name, all lowercase, no spaces — e.g. `sarah-keypair`).
  - [ ] **Key pair type** — two radio buttons: "RSA" and "ED25519". Leave **RSA** selected (it's the default).
  - [ ] **Private key file format** — two radio buttons: ".pem" and ".ppk". Leave **.pem** selected (this works with the SSH tools built into macOS, Linux, and modern Windows 10/11; only choose ".ppk" if you specifically know you'll be using the older PuTTY tool).
  - [ ] Scroll down if needed and leave **Add tag** empty — we don't need tags for this lab.
- [ ] Click the orange **Create key pair** button at the bottom of the panel.
- [ ] Your browser will immediately download a file — check your browser's downloads bar/folder for a file named `<yourname>-keypair.pem`.

> ⚠️ **This is the only time AWS will ever let you download this file.** If you lose it, AWS cannot regenerate it — you'd need to create a brand new key pair instead. Move the downloaded file somewhere you'll find it again (e.g. drag it onto your Desktop, or into your home folder), and remember exactly where you put it — you'll need its file path again shortly.

- [ ] You should now be back on the "Key Pairs" page, and a new row should appear in the table showing `<yourname>-keypair` with type "rsa" and format "pem". This confirms AWS successfully created and registered the public half of the key pair.

---

## Part 2: Launch the Instance

- [ ] In the left-hand navigation menu, click **Instances** (near the top, above "Network & Security").
- [ ] You'll see a page titled "Instances" with a table (likely empty, or showing other participants' instances if this is a shared account — that's expected). In the top-right of the page, click the orange button labelled **Launch instance**.
- [ ] You're now on the "Launch an instance" page. This is one long scrollable page, not a multi-step wizard — you'll fill in each section from top to bottom, then click one final "Launch instance" button at the very end.

### Section: Name and tags

- [ ] At the very top of the page, find the box labelled **Name**.
- [ ] Click into it and type: `<yourname>-server`.

### Section: Application and OS Images (Amazon Machine Image)

- [ ] Scroll down to the next section, titled **Application and OS Images (Amazon Machine Image)**.
- [ ] You'll see a row of tabs: "Quick Start", "My AMIs", "AWS Marketplace AMIs", "Community AMIs". The **Quick Start** tab should already be selected (highlighted).
- [ ] Below the tabs, a row of OS logos appears (Amazon Linux, macOS, Ubuntu, Windows, Red Hat, SUSE, etc.). The **Amazon Linux** logo should already be selected — it has a blue border/highlight around it. Leave it selected.
- [ ] Below that, confirm the dropdown shows an AMI name starting with **"Amazon Linux 2023 AMI"**, and that the text nearby says **"Free tier eligible"** — leave every setting in this section at its default.

### Section: Instance type

- [ ] Scroll down to the **Instance type** section.
- [ ] There's a dropdown box, likely already showing `t2.micro`. Click on it.
- [ ] A searchable list appears. Type `t3.micro` into the search box at the top of that list.
- [ ] Click on **t3.micro** from the filtered results to select it.

### Section: Key pair (login)

- [ ] Scroll down to the **Key pair (login)** section.
- [ ] Click the dropdown box (it may currently show "Select key pair" or a previously-used key pair).
- [ ] From the list that appears, click **`<yourname>-keypair`** — the exact key pair you created in Part 1.

### Section: Network settings

- [ ] Scroll down to the **Network settings** section. You'll see a summary box with a few lines of text and a button in the top-right of that box labelled **Edit**. Click **Edit**.
- [ ] The box expands to show several fields. Leave **VPC** and **Subnet** at their defaults (we're using the account's existing default VPC for this lab).
- [ ] Find **Auto-assign public IP** — confirm the dropdown shows **Enable**. If it shows "Disable", click the dropdown and change it to **Enable**.
- [ ] Scroll down slightly within this expanded section to **Firewall (security groups)**. Two radio buttons appear: "Select existing security group" and "Create security group". Confirm **Create security group** is selected.
- [ ] Just below that, two more fields appear: **Security group name - required** and **Description**.
  - [ ] Click into **Security group name - required**. It will show a greyed-out placeholder like `launch-wizard-1` — this is only placeholder text, not an actual value yet. Click into the box and type over it: `<yourname>-web-sg`.
  - [ ] The **Description** field will auto-fill with matching placeholder text — you can leave it as-is.
- [ ] Below that is an **Inbound security groups rules** table with columns: Type, Protocol, Port range, Source type, Source, Description. By default, one row already exists for SSH:
  - [ ] Confirm the **Type** column for this row shows **ssh**.
  - [ ] Confirm the **Source type** column shows a dropdown — click it and select **My IP** (not "Anywhere" — this restricts SSH access to only your current internet connection).
  - [ ] AWS will automatically detect and fill in your current public IP address in the **Source** column, shown as something like `82.14.xxx.xxx/32`.
- [ ] Click **Add security group rule** (a text link/button just below the table) to add a second rule:
  - [ ] A new row appears. Click the **Type** dropdown for this new row and select **HTTP** from the list.
  - [ ] The **Port range** column will auto-fill to `80`.
  - [ ] Click the **Source type** dropdown for this row and select **Anywhere** (this appears in the list as "Anywhere-IPv4"). The **Source** column will auto-fill to `0.0.0.0/0`.

### Section: Configure storage

- [ ] Scroll down to **Configure storage**. Leave everything at its default (typically "1x 8 GiB gp3").

### Final step: Launch

- [ ] Scroll down further and confirm there's a **Summary** panel on the right-hand side of the page showing "Number of instances: 1", the AMI, instance type, key pair name, and security group you just configured. Double-check the key pair name shown here matches `<yourname>-keypair` exactly.
- [ ] At the bottom of that Summary panel, click the large orange **Launch instance** button.
- [ ] A confirmation screen appears with a green success banner reading "Successfully initiated launch of instance". Click the instance ID link shown on that screen (it looks like `i-0abc123def456...`), or click **View all instances** to go back to the instance list.

### Wait for it to be ready

- [ ] On the Instances page, find the row for `<yourname>-server`. Two columns matter right now:
  - [ ] **Instance state** — will show "Pending" (with a small orange/yellow icon) at first, then change to **Running** (green icon) after roughly 30–60 seconds. Refresh using the circular refresh icon in the top-right of the table if it seems stuck.
  - [ ] **Status check** — will show "Initializing" at first, then change to **2/2 checks passed** after another minute or so. Wait for this before continuing — connecting too early will fail.
- [ ] Once both show green/passed, click on the **Instance ID** link for `<yourname>-server` to open its details page.
- [ ] On this details page, find the **Details** tab (should already be selected/active). Look for a field labelled **Public IPv4 address** and note down the value shown (e.g. `54.220.xxx.xxx`) — you'll need it for the next part. There's a small copy icon next to it you can click to copy it directly.

---

## Part 3: Connect via SSH

- [ ] Open a terminal application on your own computer:
  - **macOS:** open the **Terminal** app (search for it via Spotlight — Cmd+Space, then type "Terminal").
  - **Windows 10/11:** open **PowerShell** or **Windows Terminal** (search for either via the Start menu).
  - **Linux:** open your distribution's terminal application.
- [ ] In the terminal, navigate to the folder where your `.pem` file was downloaded. For example, if it's in your Downloads folder:
```bash
cd Downloads
```
- [ ] Confirm the file is actually there by listing the folder's contents:
```bash
ls
```
  (On Windows PowerShell, use `dir` instead of `ls` if `ls` doesn't work.) You should see `<yourname>-keypair.pem` in the output.

### macOS / Linux

- [ ] Lock down the key file's permissions — SSH refuses to use a key file that's readable by anyone else:
```bash
chmod 400 <yourname>-keypair.pem
```
- [ ] Connect, replacing `<public-ip>` with the exact address you copied at the end of Part 2:
```bash
ssh -i <yourname>-keypair.pem ec2-user@<public-ip>
```

### Windows 10 / 11 (PowerShell)

- [ ] Windows doesn't have `chmod` — instead, lock down the file using `icacls`, run one line at a time:
```powershell
icacls <yourname>-keypair.pem /inheritance:r
icacls <yourname>-keypair.pem /grant:r "%username%:R"
```
- [ ] Connect, replacing `<public-ip>` with the exact address you copied at the end of Part 2:
```powershell
ssh -i <yourname>-keypair.pem ec2-user@<public-ip>
```

### First connection

- [ ] The very first time you connect to any new server, you'll see a message similar to:
```
The authenticity of host '54.220.xxx.xxx' can't be established.
ED25519 key fingerprint is SHA256:xxxxxxxxxxxxx.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```
  Type `yes` and press Enter. This is expected and normal — your SSH client is simply confirming it's never spoken to this exact server before. It will remember this server going forward, and will loudly warn you instead if this fingerprint ever unexpectedly changes later (a possible sign of impersonation).
- [ ] If everything worked, your terminal prompt will change to something like:
```
       __|  __|_  )
       _|  (     /   Amazon Linux 2023
      ___|\___|___|

[ec2-user@ip-172-31-xx-xx ~]$
```
  This new prompt means you are now typing commands *on the remote server*, not your own laptop.

### Alternative — no local terminal needed

- [ ] If you're having trouble with the steps above, go back to the EC2 console, select your instance's checkbox in the Instances table, and click the **Connect** button near the top of the page.
- [ ] On the page that opens, click the **EC2 Instance Connect** tab (one of several tabs across the top: "EC2 Instance Connect", "Session Manager", "SSH client", etc.).
- [ ] Confirm the **User name** field shows `ec2-user`, then click the orange **Connect** button at the bottom.
- [ ] A new browser tab opens with a black terminal window directly connected to your instance — no `.pem` file needed for this method.
  > ⚠️ This will not work if you left the SSH security group rule scoped to "My IP" from Part 2 — it needs to be set to "Anywhere" instead, since this connection method comes from AWS's own servers, not your computer's IP. If it hangs or fails, go back to the security group (**Network & Security → Security Groups → `<yourname>-web-sg`**), edit the inbound SSH rule's source to **Anywhere-IPv4**, and try again. Treat this as a backup option — the `.pem` method above is the one this lab is built around.

---

## Part 4: Install a Simple Web Server, by Hand

You should now have a terminal prompt starting with `[ec2-user@...]$`, confirming you're connected to the remote server. Run each of the following commands one at a time, pressing Enter after each and waiting for it to finish before typing the next:

```bash
sudo dnf update -y
```
- [ ] This updates the server's installed packages. It can take 30–90 seconds — wait for your prompt to return before continuing.

```bash
sudo dnf install -y httpd
```
- [ ] This installs the Apache web server software (`httpd` is its package/service name).

```bash
sudo systemctl start httpd
```
- [ ] This starts the web server.

```bash
sudo systemctl enable httpd
```
- [ ] This ensures the web server automatically restarts if the instance ever reboots.

```bash
echo "<h1>Hello from <yourname>'s EC2 server!</h1>" | sudo tee /var/www/html/index.html
```
- [ ] Replace `<yourname>` in this command with your actual name before running it. This creates a simple webpage the server will display. After running it, the command will echo the same line back to your terminal — that's expected, confirming the file was written.

### Verify it worked

- [ ] Open a web browser on your own computer (not inside the terminal) and go to: `http://<public-ip>` (the same IP address from Part 2, no `https://`, just `http://`).
- [ ] You should see a plain webpage displaying "Hello from `<yourname>`'s EC2 server!" in large heading text.
- [ ] Back in your terminal, type `exit` and press Enter to close the SSH connection and return to your own computer's terminal.

---

## EC2 Concepts Learned

- Regions and Availability Zones, and why service quotas are region-specific
- Amazon Machine Images (AMIs) — AWS's own Quick Start images
- Instance types
- **SSH key pairs** — how the public/private key split works, and why the private key file must never be shared
- Security groups (stateful virtual firewalls), including restricting SSH to **My IP** rather than the whole internet
- Connecting to a running instance via SSH, and installing software manually on it

---

## Troubleshooting

- **"Permission denied (publickey)" when connecting:** almost always means either the wrong username (must be `ec2-user` for Amazon Linux, all lowercase) or the key file's permissions weren't locked down — re-run `chmod 400 <yourname>-keypair.pem` (macOS/Linux) or the two `icacls` commands above (Windows). Also double-check you're pointing at the correct `.pem` file if you've created more than one during this course.
- **"Connection timed out" when connecting:** almost always a security group problem. Go to **EC2 → Network & Security → Security Groups**, click `<yourname>-web-sg`, click the **Inbound rules** tab, and confirm there's a rule for SSH (port 22) with your current IP as the source. If your IP has changed since launch (e.g. you've switched WiFi networks), click **Edit inbound rules**, update the SSH rule's source to **My IP** again (this refreshes it to your current address), and click **Save rules**.
- **Browser shows nothing at `http://<public-ip>`:** back in your SSH session, run `sudo systemctl status httpd` and confirm it says "active (running)" in green text. Also confirm the security group's inbound rules include HTTP (port 80) from `0.0.0.0/0`.
- **Lost or deleted your `.pem` file:** AWS cannot re-issue the private half of an existing key pair — the only fix is to create a new key pair (Part 1) and launch a new instance with it.
- **Any "LimitExceeded" or quota error while launching:** go back to the top-right region selector and confirm it still says **Ireland** — quotas were only raised in `eu-west-1`.
- **Terminal shows "command not found: ssh" (Windows only):** use **PowerShell**, not the older Command Prompt (`cmd.exe`) — modern Windows 10/11 PowerShell includes SSH built in, but very old Command Prompt versions may not.

---

## Cleanup — Do This Before Ending the Session

- [ ] If still connected via SSH, type `exit` and press Enter.
- [ ] In the EC2 console, go to **Instances**, tick the checkbox next to `<yourname>-server`.
- [ ] Click **Instance state** (a dropdown button near the top of the page) → **Terminate instance**.
- [ ] A confirmation dialog appears warning that any data will be lost — click the orange **Terminate** button to confirm.
- [ ] Wait for the **Instance state** column to show **Terminated** (this can take up to a minute) before moving to the next step.
- [ ] Go to **Network & Security → Security Groups** in the left-hand menu, tick the checkbox next to `<yourname>-web-sg`, and click **Actions → Delete security group** (top-right). Confirm in the dialog that appears. If this fails with an error saying it's still in use, your instance likely hasn't finished terminating yet — wait another minute and try again.
- [ ] Go to **Network & Security → Elastic IPs** and confirm there's nothing listed with your name — if there is and it shows "Not associated", tick its checkbox and click **Actions → Release Elastic IP addresses**.
- [ ] *(Optional)* The **`<yourname>-keypair`** key pair itself costs nothing to leave in your account and can be safely reused in a later lab if you still have the `.pem` file — no need to delete it unless your trainer asks for a full account tidy-up.