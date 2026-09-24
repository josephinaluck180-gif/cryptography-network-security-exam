# Risk Assessment:

### a. Threat Matrix (Assets, Vulnerabilities, & Consequences)
1. **Asset:** Student Academic and Personal Records Database.
   * **Vulnerability:** Guest network access permitted to the records server.
   * **Consequence:** Unauthorized data exposure, data tampering, or identity theft of students.
2. **Asset:** Inter-Campus File Transfer Pipeline.
   * **Vulnerability:** Unencrypted file transfer protocols (e.g., FTP/HTTP).
   * **Consequence:** Man-in-the-Middle (MitM) eavesdropping, allowing credentials or records to be intercepted in transit.
3. **Asset:** Central Server Administrative Access.
   * **Vulnerability:** Weak staff passwords and outdated operating system/software.
   * **Consequence:** Brute-force compromise leading to full server takeover or Ransomware deployment.

### b. Risk Ranking (Likelihood & Impact)
1. **Rank 1: Guest Network Access to Records Server**
   * **Reasoning:** High Likelihood / Critical Impact. Anyone on campus can connect. Exploitation requires zero technical skill and immediately exposes sensitive data.
2. **Rank 2: Weak Staff Passwords & Outdated Software**
   * **Reasoning:** High Likelihood / High Impact. Automated external scanning (already observed) will eventually guess weak credentials or exploit unpatched vulnerabilities.
3. **Rank 3: Unencrypted Inter-Campus File Transfers**
   * **Reasoning:** Medium Likelihood / High Impact. Requires network visibility between campuses, but exposes all moving records directly if intercepted.

### c. Recommended Controls
1. **Control 1 (For Guest Access):** Implement network segmentation using VLANs and strict firewall Access Control Lists (ACLs) to isolate the database server.
2. **Control 2 (For Weak Passwords/Software):** Enforce a strong Password Policy, deploy Multi-Factor Authentication (MFA), and establish an automated patch management schedule.
3. **Control 3 (For Unencrypted Transfers):** Mandate the use of secure protocols like SFTP or HTTPS leveraging TLS/SSL.
