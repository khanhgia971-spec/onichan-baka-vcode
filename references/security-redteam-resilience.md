# Principal Security Officer (`/cso`) & Authorized Local Stress-Testing Playbook

> **STRICT AUTHORIZATION BOUNDARY**: All penetration testing, fuzzing, and high-concurrency stress/load testing (`/redteam-audit`) MUST be executed exclusively against `localhost`, `127.0.0.1`, local Docker containers, or staging environments explicitly owned by the user. Never target external third-party domains.

## 1. Red-Team Vulnerability Audit (OWASP Top 10 + STRIDE)

Act as a 40-year Principal Application Security Engineer. Before any release (`/ship`), audit the codebase across 6 adversarial vectors and automatically fix every discovered flaw:

1. **Broken Access Control & IDOR (Spoofing / Elevation of Privilege)**:
   - Verify every API route and server action checks object-level ownership (`user_id == resource.owner_id`) and role permissions on the server side, never trusting client headers or JWT claims without signature verification.
2. **Injection & Deserialization (Tampering)**:
   - Audit all SQL, NoSQL, GraphQL, OS command (`child_process`, `subprocess`), and template rendering paths. Enforce parameterized queries, strict Zod/Pydantic schemas, and zero raw string concatenation.
3. **Authentication, Session & Cryptographic Failures (Information Disclosure)**:
   - Check password hashing (`Argon2id` / `bcrypt`), short-lived JWT rotation, `HttpOnly; Secure; SameSite=Strict` cookies, CSRF tokens, and `.env` secret leakage in client bundles (`NEXT_PUBLIC_`, `VITE_`).
4. **SSRF, Path Traversal & File Upload Exploits**:
   - Validate all user-supplied URLs against private IP ranges (`127.0.0.0/8`, `10.0.0.0/8`, `169.254.169.254`) and sanitize file paths with `path.resolve` boundary checks.
5. **Race Conditions & TOCTOU (Time-of-Check to Time-of-Use)**:
   - Audit financial balances, inventory decrements, coupon redemptions, and quota counters. Enforce database row-level locking (`SELECT ... FOR UPDATE`), atomic SQL increments, or Redis Lua scripts.

## 2. Local Resilience & Application-Layer Stress Testing (Anti-DoS Hardening)

To verify the user's web app or API can survive traffic spikes and application-layer DoS patterns on `localhost`:

1. **Automated Local Load Probe**:
   - Run bounded local stress tests against `http://localhost:<port>` using `npx autocannon -c 100 -d 15 http://localhost:3000/api/health` or `k6` / `locust`.
2. **Bottleneck & Exhaustion Detection**:
   - Check for event-loop blocking, unindexed database scans, connection-pool exhaustion, memory leaks, and Regular Expression Denial of Service (ReDoS).
3. **Mandatory Defensive Hardening Fixes**:
   - Add token-bucket / sliding-window rate limiting (e.g., per-IP and per-user limits on auth and expensive endpoints).
   - Enforce strict request body size limits (e.g., `1MB` JSON cap), query complexity/depth limits, request timeouts (`AbortSignal.timeout`), and circuit breakers.
   - Record all discovered vulnerabilities and their verified fixes in `.ai-memory/BUG_LEDGER.md`.
