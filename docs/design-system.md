# Design system: tokens

The UI is Apple-inspired glass: layered translucent surfaces over a soft wallpaper, capsule controls and an 8 pt grid. It is neutral first, and colour always carries meaning.

## Typography

| Role | Spec |
|---|---|
| UI font | `-apple-system, "SF Pro Text", "Geist", system-ui` |
| Mono (IDs, invoice numbers, times) | `"SF Mono", "Geist Mono", ui-monospace` |
| Greeting | 40–56 px / 700 / −4% tracking |
| Page title | 32 px / 700 / −3% |
| Card title | 15 px / 650 |
| Body | 13 px / 1.45 |
| Meta | 12–12.5 px, secondary colour |
| Numbers | Always `font-variant-numeric: tabular-nums` |

## Colour

### Neutrals (Apple system-style)

| Token | Value |
|---|---|
| Label | `#1D1D1F` |
| Secondary label | `#6E6E73` |
| Tertiary label | `#86868B` / `#8E8E93` |
| Fill | `rgba(118,118,128,.12)` |
| Separator | `rgba(60,60,67,.08–.12)` |
| Wallpaper base | `#EDF0F4`, with pale blue, lilac and sand radial washes |

### Brand (Van Amstel Business Tech)

| Token | Value | Use |
|---|---|---|
| Ink | `#0B0C0F` / `#1D1D1F` | Primary buttons, active filters, logo mark |
| Sand | `#D1C1A3` | AI mark, soft brief glow, brief dot |
| Bronze | `#7A6440` / `#5E4C2E` | Accent text on sand tints |

### Status

| Meaning | Fill | Text |
|---|---|---|
| Success / on track / paid | `rgba(52,199,89,.15)` | `#1E7B34` |
| Warning / at risk / follow-up | `rgba(255,149,0,.16)` | `#A2520A` |
| Danger / behind / overdue | `rgba(255,59,48,.12)` | `#C4241B` |
| Info / active / sent | `rgba(0,122,255,.11)` | `#0060C8` |
| Milestone / proposal | `rgba(48,176,199,.15)` | `#0B6E80` |
| Review / appointment | `rgba(209,193,163,.34)` | `#5E4C2E` |

### Calendar event types

| Type | Dot | Chip |
|---|---|---|
| Meeting | `#007AFF` | blue tint, `#0050A8` text |
| Follow-up | `#FF9500` | orange tint |
| Deadline | `#FF3B30` | red tint |
| Milestone | `#30B0C7` | teal tint |
| Task | `#AEAEB2` | grey tint |

## Surfaces

| Surface | Recipe |
|---|---|
| Sidebar (`.glass`) | `rgba(255,255,255,.56)`, `blur(40px) saturate(180%)`, 1 px white border, radius 24 |
| Window (`.sheet`) | `rgba(255,255,255,.5)`, `blur(36px)`, radius 24 |
| Card | `rgba(255,255,255,.8)`, hairline shadow + `0 8px 28px rgba(30,40,70,.06)`, radius 18 |
| Menu / drawer / modal | `rgba(255,255,255,.8–.84)`, `blur(30–40px)`, radius 14 / 24 / 24 |

## Shape and spacing

- **Spacing:** 4, 8, 12, 16, 20, 24, 32. Page padding is 28/32, and cards sit 20 apart.
- **Radius:** 999 for buttons, chips, tabs, badges and search; 18 for cards; 24 for sheets and drawers.
- **Controls:** 32 px default and 28 px small. Checkboxes are round (Reminders style).
- **Motion:** content rises 8 px over 0.45 s, drawers slide in from the right, and nothing loops.
