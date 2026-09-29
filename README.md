# Business OS

A high-fidelity, interactive prototype of a **Business Operating System** for Van Amstel Business Tech: one connected system for CRM, clients, projects, tasks, calendar, finance, documents, team and an AI Daily Brief.

> **Status:** UX/UI prototype. There is no backend, database or authentication, and all data is realistic mock data.

## View the prototype

The live, clickable prototype is a Claude Design canvas:
**https://claude.ai/artifact/ELgJjLkNWs3aiWbdo6sUCS**

The link opens straight into the interactive prototype. It is private until the owner shares it from the **Share** menu.

## What's in this repo

```
design/
  canvas.json                  Canvas layout: board positions, titles, launch view
  Main.dc.html                 The interactive prototype (source of truth)
  01-Dashboard.dc.html …       One full-length board per page, generated from Main
  19-Convert-lead.dc.html      Detail views and overlays
  Architecture.dc.html         Information architecture, entity model, key flows
  DesignSystem.dc.html         Foundations and components
docs/
  product.md                   Product concept, pages and flows
  design-system.md             Tokens: colour, type, spacing, radius, glass
CONTRIBUTING.md                How we work on this together
```

Each `.dc.html` file is a self-contained *Design Component* page: HTML markup with `{{holes}}` and one `class Component extends DCLogic` script that holds the mock data, state and interactions. The files render inside the Claude Design canvas.

### One source, many boards

`design/Main.dc.html` is the only file you edit by hand. Every page board (`01-…` to `19-…`) is a copy of it with two different defaults:

| Prop | What it does | Example |
|---|---|---|
| `screen` | Which page or state the board opens on | `crm`, `project`, `taskDrawer`, `convert` |
| `frameH` | Board height in px, so the whole page fits without scrolling | `1450` |

After changing `Main.dc.html`, regenerate the boards (see CONTRIBUTING.md) so every page stays in sync.

## Pages

1. Dashboard
2. CRM (leads)
3. Clients
4. Projects
5. Tasks
6. Calendar
7. Finance
8. Documents
9. Team
10. AI Daily Brief (replaces notifications)

It also has detail views for leads, clients, projects, invoices, documents and team members, plus drawers for tasks and events, a lead-to-client conversion flow and focus mode.

## Flows that work end to end

- **Sales to delivery:** Dashboard → CRM → Lead → *Convert to client* → Client → Project → Task → Calendar
- **Client 360:** Client → Project → Documents → Finance → Invoice
- **Delivery:** Project → Tasks → change deadline → the task moves in the Calendar → Team member
- **AI-first morning:** Dashboard → Daily Brief → *Focus mode* → handle each item one at a time
- **Undo:** completing a task, marking an invoice paid or dismissing a brief item can be undone from the notification

## Design direction

Clean, Apple-inspired glass UI: frosted sidebar and window, capsule controls, an 8 pt grid and SF Pro (Geist as fallback). Neutral first, with the Van Amstel ink `#0B0C0F` and sand `#D1C1A3` as restrained brand accents. See [docs/design-system.md](docs/design-system.md).
