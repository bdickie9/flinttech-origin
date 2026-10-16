# FLINTTECH brand specification

Version 1.0 · 16 October 2026 · Reference-led implementation specification

## 1. Source and interpretation

The supplied reference, IMG_0202.jpeg, is 784 × 1168 pixels. It shows a nearly black indigo field, a single long tapered vertical white spark, violet bloom, generous empty space, and a widely spaced white FLINTTECH wordmark below the spark.

Pixel observations from the unchanged JPEG: upper-left at (20,20) is #070314; upper center at (390,50) is #0E061E; spark center at (390,550) is #FFFFFF; nearby violet at (360,550) is #7247A1. These are samples from a compressed image with gradients, not official flat brand colors.

The values below are normalized design choices derived from that visual direction. The SVGs are new vector reconstructions, not recovered original artwork. The exact font, original logo geometry and original color specification are not known.

## 2. Identity

- Master brand: FLINTTECH, uppercase in the wordmark.
- Signature: one slender vertical spark, sharp at both ends, white at its core.
- Atmosphere: deep indigo with restrained violet illumination.
- Layout: deliberate space, few competing elements, crisp typography.
- Avoid introducing extra orbit rings, infinity badges, circuit diagrams, lens flares or multi-color gradients as competing brand marks.
- Preserve existing product names in the rollout. Use the FLINTTECH lockup with a smaller product label: FLINT CONTINUUM or Singularity. The Base44 editor name everlastAI and the public name Singularity are observed aliases; this kit does not rename either.
- The separately designed Flint Spark companion is an optional personality asset. It is not a substitute for the corporate spark mark.

## 3. Palette

| Role | Token | Value | Use |
|---|---|---|---|
| Field | `--ft-background` | #090513 | Main dark canvas |
| Surface | `--ft-surface` | #141020 | Panels, inputs |
| Raised | `--ft-raised` | #1D162E | Hovered or elevated surfaces |
| Primary text | `--ft-text` | #F7F4FF | Headings and body |
| Secondary text | `--ft-muted` | #BDB3CF | Labels and supporting copy |
| Violet | `--ft-accent` | #B782FF | Brand accent, decorative bloom |
| Action | `--ft-action` | #C5A3FF | Filled buttons and links |
| Action hover | `--ft-action-hover` | #D8C2FF | Hover state |
| Action text | `--ft-ink` | #100B1A | Text on filled light-violet buttons |
| Decorative border | `--ft-border` | #362847 | Nonessential panel division only |
| Control border | `--ft-control-border` | #827294 | Visible input and secondary-button boundary |
| Focus | `--ft-focus` | #E3C8FF | 3px focus outline with 4px offset |

Functional status colors are #96E3BC (success), #FFD79A (review/warning), and #FFB3BD (error). Pair every status with explicit text or an icon plus an accessible name. Use violet for brand meaning, not every semantic status.

Do not place white text on the light-violet action fill. Use the dark ink token. Do not use the decorative border as the only boundary that identifies a required control. Check every alpha-blended or gradient context separately; the token checks only cover opaque pairs.

## 4. Typography and spacing

Use a clear sans-serif. The supplied component uses Arial/Helvetica for a practical wordmark approximation and Inter if already present, with system sans-serif fallbacks, for interfaces. No new remote font request is required. This is not an exact-font identification.

- Wordmark: medium weight, uppercase, approximately 0.30em letter spacing; no extreme stretching.
- Body: 16px minimum in normal layouts, 1.6 line height.
- Supporting labels: generally 12–14px; avoid 8–10px operational copy.
- Use wide tracking for the logo and short labels only. Sentence-case content and normal body tracking improve scanning.
- Suggested spacing steps: 4, 8, 12, 16, 24, 32, 48 and 64px.
- Control radius: 8px. Panel radius: 12px. Use shallow borders instead of heavy card shadows.
- Keep wordmark clear space at least one cap-height around a standalone lockup.
- At narrow sizes, stack the product label below the master brand; avoid squeezing or clipping the wordmark.

## 5. Spark and image use

- Use `spark.svg` for a hero or cover, in an empty area away from body text. Its viewBox includes its halo.
- Use the flat compact mark in navigation and `favicon.svg` for small browser icons. Small-size geometry is intentionally wider for readability.
- White is the default mark on dark surfaces. Use a solid dark version on light print surfaces; omit glows in print.
- Do not add decorative motion by default. A still, precise spark is the base experience.
- Do not stretch the SVG disproportionately. `lockup.svg` retains editable text; font fallback can alter its appearance. The React/live-text lockup is preferred in applications.
- A decorative spark beside visible brand text has empty alt text or `aria-hidden="true"`. A standalone linked mark must have a meaningful accessible name such as “FLINTTECH home.”

## 6. Accessibility requirements

Text should meet at least 4.5:1 contrast for ordinary sizes, or 3:1 for qualifying large text. The included palette aims above those minima on the specified dark surfaces. Thin strokes and transparency still need real rendering review. [W3C: Contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)

Essential control boundaries and information-bearing graphics should have at least 3:1 contrast against adjacent colors. Decorative separators may be subtler when they are not required to identify a control or understand its state. [W3C: Non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)

Keep keyboard focus visible; retain native labels and button semantics. Target 44px minimum controls as this kit's usability standard. Check keyboard use, text resizing, narrow layouts, error messages, screen-reader naming and forced-colors mode during integration. Color tests alone do not establish WCAG conformance.

Honor `prefers-reduced-motion` and remove nonessential interaction animation. The kit has no perpetual decorative animation. This follows the intent of the W3C guidance on disabling motion that is not essential. [W3C: Animation from interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)

## 7. Content integrity

Brand quality includes accurate system state. Keep “prototype,” “not connected,” “sample data,” and disabled-action language where it reflects reality. Do not turn a mockup into an implied live operational claim. Avoid inventing performance, customer, earnings, payment or ownership proof in visual polish.

## 8. Surfaces beyond the app

- Documents and proposals: FLINTTECH lockup, a quiet violet rule and clear section hierarchy. Use a light paper background with dark text for long print documents.
- Reports and dashboards: reserve glow for the opening/brand area. Keep data cells flat, high-contrast and labeled.
- Email signatures: text-first FLINTTECH identity and one modest mark; no animated signature.
- Social/cover images: centered spark with white wordmark, generous clear space, safe cropping.
- External account avatars and logos: map the account owner and required asset dimensions before changing them. This kit makes no account changes.
