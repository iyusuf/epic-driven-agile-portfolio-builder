# 📚 Learning Tracker & Delivery Plan

This file tracks all learning and portfolio-building progress across epics, grouped by project phase. Use this as your master index to stay focused and outcome-driven.

---

## 🧠 Platform-Wide Vision & Goals

> 🤖 **Vision:** Build a platform that can eventually be operated by a Local LLM agent under Model Context Protocol (MCP), enabling developers to spin up infra on demand, compliantly, and securely, using natural language or domain requests.
>
> **Strategic Objectives:**
>
> * Groundwork for real-world agentic systems work
> * Provisioning and configuration as part of a platform engineering initiative to help a small team (5–10 developers) self-serve fully bootstrapped infrastructure with CI/CD and test automation
> * Rapid skeleton service generation directly from OpenAPI contracts, staying current with evolving change requests or new features arriving mid-sprint
> * Clean architecture conformance — automatically generating package structure and validation tests to ensure strict adherence to domain-driven design and architectural boundaries

---

## 🔧 Phase 0: Infrastructure Readiness 🐳

[📖 View Full Phase 0 Document](PHASE-0.md)

| Epic ID | Title                                 | Tag                 | Status         | Git Repo / Folder                   | Demo Video Link |
| ------- | ------------------------------------- | ------------------- | -------------- | ----------------------------------- | --------------- |
| 0.1     | Provision and Bootstrap Dev Infra     | 🐳 Infra/Foundation | 🔄 In Progress | `/infra/terraform`                  | *TBD*           |
| 0.2     | Local Container Stack + Dev Bootstrap | 🐳 Infra/Foundation | 🔄 In Progress | `/infra/scripts/` + `/swarm/`       | *TBD*           |
| 0.3     | GitOps + DevOps-Ready Repo Design     | 🐳 Infra/Foundation | 🔄 In Progress | `/infra/registry/` + root structure | *TBD*           |

---

## 🧱 Phase 1: Core Architecture Foundation

| Epic ID | Title                                 | Tag                  | Status      | Git Repo / Folder            | Demo Video Link |
| ------- | ------------------------------------- | -------------------- | ----------- | ---------------------------- | --------------- |
| 1       | Domain-Driven Design for BPG          | 🧱 Core Architecture | 🔜 To Start | `/backend/merchant-service/` | *TBD*           |
| 2       | Clean Architecture in Payment API     | 🧱 Core Architecture | 🔜 To Start | `/backend/payment-api/`      | *TBD*           |
| 3       | Event-Driven Microservices            | 🧱 Core Architecture | 🔜 To Start | `/backend/event-bus/`        | *TBD*           |
| 12      | Spring Data JDBC Showcase             | 🧱 Core Architecture | 🔜 To Start | `/backend/jdbc-demo/`        | *TBD*           |
| 17      | Java Interview-Ready Microservice Kit | 🧪 Interview Prep    | 🔜 To Start | `/backend/interview-kit/`    | *TBD*           |

---

## 🔄 Phase 2: Eventing, Data, and Security

| Epic ID | Title                         | Tag                  | Status      | Git Repo / Folder          | Demo Video Link |
| ------- | ----------------------------- | -------------------- | ----------- | -------------------------- | --------------- |
| 5       | Multi-Tenant Authorization    | 🧱 Core Architecture | 🔜 To Start | `/backend/authz/`          | *TBD*           |
| 6       | CBS Integration Flow          | 🧱 Core Architecture | 🔜 To Start | `/backend/cbs-connector/`  | *TBD*           |
| 10      | Redis Session/Consent Mgmt    | 🧱 Core Architecture | 🔜 To Start | `/backend/session-cache/`  | *TBD*           |
| 11      | MongoDB for Audit/Event Store | 🧱 Core Architecture | 🔜 To Start | `/backend/auditlog/`       | *TBD*           |
| 13      | Kafka Dev Playground          | 🧱 Core Architecture | 🔜 To Start | `/backend/kafka-demo/`     | *TBD*           |
| 15      | GitLab CI/CD Pipeline         | 🐳 Infra/Foundation  | 🔜 To Start | `/ci/` or `.gitlab-ci.yml` | *TBD*           |

---

## 🧠 Phase 3: AI-Enhanced BPG Platform

| Epic ID | Title                              | Tag               | Status      | Git Repo / Folder           | Demo Video Link |
| ------- | ---------------------------------- | ----------------- | ----------- | --------------------------- | --------------- |
| 18      | LLM-Enabled API Assistant          | 🧠 AI Integration | 🔜 To Start | `/ai/api-assistant/`        | *TBD*           |
| 19      | Agentic Onboarding Reviewer        | 🧠 AI Integration | 🔜 To Start | `/ai/onboarding-agent/`     | *TBD*           |
| 20      | AI Chat Overlay for Angular Admin  | 🧠 AI Integration | 🔜 To Start | `/frontend/admin-ui/`       | *TBD*           |
| 21      | Email-to-Workflow LLM Integration  | 🧠 AI Integration | 🔜 To Start | `/ai/email-agent/`          | *TBD*           |
| 22      | Local Banking FAQ Chatbot          | 🧠 AI Integration | 🔜 To Start | `/ai/faq-bot/`              | *TBD*           |
| 23      | Visual Prompt Builder              | 🧠 AI Integration | 🔜 To Start | `/frontend/prompt-builder/` | *TBD*           |
| 24      | Keycloak-Aware Agent Authorization | 🧠 AI Integration | 🔜 To Start | `/ai/auth-scope-check/`     | *TBD*           |

---

## 🌟 Legend

* 🧱 Core Architecture
* 🐳 Infra/Foundation
* 🧠 AI Integration
* 🧪 Interview Prep
* 🚀 Showcase Ready
