---
name: planning-skill
description: Generates free loopback IP addresses from a subnet using MySQL lookup and deterministic IP computation.
---

## Overview

The planning-skill allocates free loopback IP addresses from a given subnet.

It performs the following steps:
1. Retrieves already used loopback IPs from a MySQL database
2. Computes available IP addresses inside the subnet
3. Returns the requested number of free IPs

Use this skill whenever the user requests free loopback IP addresses.

---

## Input validation rules

- `subnet` MUST be in CIDR format (example: 18.197.124.0/24)
- If subnet is NOT in CIDR format:
  - do NOT proceed
  - ask user to provide a valid CIDR subnet
- Do NOT attempt to infer or fix invalid subnets

---

## Tools

### send_sql_command(sql_query: str)
Executes a SQL query and returns a list of used loopback IP addresses from the database.
If the result set exceeds the configured maximum size, the tool also stores the complete SQL result as an artifact.

### calculate_free_ips(
    number_of_addresses,
    subnet,
    used_loopback_ips,
)
Calculates the requested number of free IP addresses. 
The tool automatically loads the complete SQL result from the artifact created by `send_sql_command` 
when one exists. Otherwise, it uses the `used_loopback_ips` returned by `send_sql_command`.

---

## Database Schema

Primary table: `dev_radio_data`

Relevant column:
- `loop_ip` (TEXT): loopback IP address

---

## Execution Flow

### 1. Extract input
From the user request, extract:
- `subnet` (CIDR format, e.g. 158.98.202.0/24)
- `number_of_addresses`

If either value is missing, ask the user.

---

### 2. Build SQL query (MySQL-compatible)

Generate a valid MySQL query that retrieves every allocated loopback IP address.

Example:

```sql
SELECT loop_ip
FROM dev_radio_data
WHERE loop_ip IS NOT NULL;
```

Ensure SQL is valid and safe before execution.

---

### 3. Execute the query
Call: 
`send_sql_command(sql_query)`

The tool returns the allocated loopback IP addresses.
If the result set is large, it may also create an artifact containing the complete SQL result.

---

### 4. Calculate free addresses

Call:

`calculate_free_ips(...)`

using:

- `number_of_addresses`
- `subnet`
- `used_loopback_ips` returned by `send_sql_command`

Do not inspect or load artifacts yourself. The tool handles this automatically.

Do not calculate free IP addresses manually.

---

### 5. Return the result

Return the free loopback IP addresses produced by calculate_free_ips.

If fewer addresses are available than requested, clearly state how many addresses are available and return those addresses.




