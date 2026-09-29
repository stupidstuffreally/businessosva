# Working on Business OS together

## Two places, two jobs

| Where | Use it for |
|---|---|
| **Claude Design canvas** (link in README) | Looking at the prototype, clicking through flows, visual edits, comments |
| **This GitHub repo** | Version history, reviewing changes, keeping the source files safe |

The canvas is where the prototype runs. The repo is the record of every version.

## Everyday workflow

1. **Pull first:** `git pull` before you start.
2. **Branch:** `git checkout -b short-description`, for example `calendar-colours`.
3. **Edit `design/Main.dc.html`:** layout lives in the markup, and data and behaviour live in the `Component` script at the bottom.
4. **Regenerate the page boards** so every board matches Main:
   ```bash
   python3 scripts/generate_boards.py
   ```
5. **Commit and open a pull request:** describe what changed and which flow it affects.
6. **Publish to the canvas:** once merged, ask Claude (in Cowork or Claude Code) to publish the `design/` files to the canvas link, or paste them into the canvas.

## Conventions

- **Mock data** lives in `seed()` in the script. Keep names, companies and amounts realistic: no lorem ipsum.
- **"Today"** in the prototype is fixed at Monday 28 September 2026 (`this.TODAY`), so dates stay consistent.
- **Colours:** use the tokens in `docs/design-system.md`. Colour is for status, priority, money and the one primary action; everything else stays neutral.
- **Accessibility:** use real `<button>`/`<a>`/`<input>` elements, and keep text contrast at 4.5:1 or better.
- **Don't edit `01-…`–`19-…` boards by hand.** They are overwritten by the generator.

## Board list

The generator reads `design/canvas.json` and maps each board to a screen:

| Board | `screen` |
|---|---|
| 01-Dashboard | `dashboard` |
| 02-CRM | `crm` |
| 03-Clients | `clients` |
| 04-Projects | `projects` |
| 05-Tasks | `tasks` |
| 06-Calendar | `calendar` |
| 07-Finance | `finance` |
| 08-Documents | `documents` |
| 09-Team | `team` |
| 10-AI-Daily-Brief | `brief` |
| 11-Lead-detail | `lead` |
| 12-Client-detail | `client` |
| 13-Project-detail | `project` |
| 14-Invoice-detail | `invoice` |
| 15-Document-detail | `doc` |
| 16-Team-member | `member` |
| 17-Task-drawer | `taskDrawer` |
| 18-Event-drawer | `eventDrawer` |
| 19-Convert-lead | `convert` |
