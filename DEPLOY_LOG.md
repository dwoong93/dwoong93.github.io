# Deploy log

Plain record of every change to this site, so it's easy to trace if something breaks.

## 2026-11-19 — First version of the portfolio
- **Branch:** `add-portfolio` (to be merged into `main` only after Daryl approves)
- **Added:** `index.html` — the full portfolio page (self-contained: styles, scripts and images are inside the file).
- **Source:** same content as the Claude artifact version of the portfolio, version 56.
- **Privacy checks done before publishing:** no phone number; WeRide screens have addresses, maps, receipt/order numbers and driver details blurred; roadmap feature names and trial banner blurred; Exercise Log profile screen left out.
- **To go live:** merge into `main`, then Settings → Pages → Deploy from branch → `main` / root.

## 2026-11-19 — Light/dark mode toggle
- **Branch:** `add-theme-toggle` (merge into `main` only after Daryl approves)
- **Changed:** `index.html` — added a round sun/moon button in the top-right corner that switches between light and dark mode. The page still follows the visitor's system setting until they click it; their choice is remembered in their own browser.
- **Source:** Claude artifact version 57.

## 2026-11-19 — Payment flow diagram tidy-up
- **Branch:** `add-theme-toggle` (added to the same pull request, since both change `index.html`)
- **Changed:** `index.html` — redrew the "simplified payment flow" diagram in the wallet payments case so the arrows to "Auto refund" and "Top-up charge" have room and run straight into their boxes; moved the "if top-up fails" label so it isn't cut off.
- **Source:** Claude artifact version 58.

## 2026-11-19 — Profile photo
- **Branch:** `add-theme-toggle` (same pull request #2)
- **Changed:** `index.html` — added Daryl's profile photo next to his name, in a circle with a green border. It's set as a background (not an image element) with right-click and long-press saving turned off, so it can't be opened in a new tab from the page.
- **Source:** Claude artifact version 59.
- **Follow-up:** re-centred the photo inside the circle (it was taken slightly off-centre). Claude artifact version 60.
- **Follow-up:** nudged the photo half a step back to the left, per Daryl. Claude artifact version 61.

## 2026-11-19 — Protect all images
- **Branch:** `add-theme-toggle` (same pull request #2)
- **Changed:** `index.html` — turned off right-click menus, dragging and phone long-press saving on every screenshot, the enlarged image view and the profile photo, so "Open image in new tab" and "Save image" aren't offered. Clicking to enlarge still works. Claude artifact version 62.

## 2026-11-19 — WeRide ride history screen
- **Branch:** `add-theme-toggle` (same pull request #2)
- **Changed:** `index.html` — cropped the ride history screen in the wallet payments case to show only the recorded trip (10 March 2025, completed), dropping the cancelled-and-refunded trip. Addresses stay blurred. Claude artifact version 63.
- **Follow-up (Daryl's request):** restored the full ride history screen and unblurred the 10 March 20:00 trip, so its pickup (258B Punggol Field) and drop-off (Ark Bloc) addresses are now visible. The 11:18 trip stays blurred. Claude artifact version 64.
- **Follow-up (Daryl's request):** in the ride history screen, every trip is now visible (dates, statuses, pins) and only the address and place-name lines are blurred, including for the 10 March 20:00 trip. Claude artifact version 65.
- **Follow-up:** ride history caption shortened to "Ride history page." Claude artifact version 66.
- **Follow-up:** Grab migration timeline — centred "SEP 2026" and "Handover" under the last milestone dot, like the others. Claude artifact version 67.
- **Follow-up:** PulseSync case — added that Daryl designed the graphics for the Gym Tonic training guide. Claude artifact version 68.

## 2026-11-19 — Gym Tonic training guide materials
- **Branch:** `add-theme-toggle` (same pull request #2)
- **Changed:** `index.html` — PulseSync case now shows Daryl's training-guide work in a tabbed viewer: tablet screens he redrew in Illustrator, stills from the how-to videos he filmed with a trainer, and two improved guide pages. Bullet reworded to match. Also fixed the tab script so each tab group only switches its own panels. Claude artifact version 69.
- **Follow-up:** PulseSync case — added a "Sites" tab with two photos of Gym Tonic centres Daryl commissioned (credited "Photo: Gym Tonic"), and a bullet: oversaw machine deliveries, then set up and configured the tablets. Claude artifact version 70.
- **Follow-up:** "Sites" tab — added a third commissioned site, and blurred every face in all three site photos (clients and trainers). Claude artifact version 71.
- **Follow-up:** stronger, wider blur on the face of the trainer in purple in the third site photo. Claude artifact version 72.
- **Follow-up:** renamed the "More highlights" section to "Beyond the brief" (heading and contents list). Claude artifact version 73.

## 2026-11-19 — Theme switch moved next to the name
- **Branch:** `move-theme-toggle` (merge into `main` only after Daryl approves)
- **Changed:** `index.html` — the light/dark switch moved from the top-right corner to sit right after "Daryl Woong", and now shows a label ("Light mode" / "Dark mode") next to the icon so it's easier to notice. Claude artifact version 74.
- **Follow-up:** replaced the labelled button with a sliding toggle switch (sun on the left, moon on the right, a round knob that slides between them), no text. Claude artifact version 75.

## 2026-11-19 — Visitor stats (GoatCounter)
- **Branch:** `add-analytics` (merge into `main` only after Daryl approves)
- **Changed:** `index.html` — added the GoatCounter script at the very end of the page. Stats are at https://dwoong.goatcounter.com (visits, referrer, rough country and device; no cookies, no names).
- **Per-application links:** each resume uses its own link, e.g. `https://dwoong93.github.io/?ref=armorbearer`. GoatCounter reads the `?ref=` value and shows it under "Top referrers", so you can see which company's resume link was opened.
- **Important for future updates:** this script is only in the GitHub version (the Claude artifact blocks outside scripts). When `index.html` is replaced with a new artifact export, re-append the two lines at the bottom of this file's current version.

## 2026-11-19 — Link previews (LinkedIn, WhatsApp, etc.)
- **Branch:** `add-link-preview` (merge into `main` only after Daryl approves)
- **Changed:** `index.html` — wrapped the page in a full HTML document (`<!doctype>`, `<head>`, `<body>`) with a title, description and Open Graph / Twitter preview tags, plus the small base styles the Claude artifact host normally adds. LinkedIn couldn't build a preview before because the file had no `<head>`.
- **Added:** `og-image.png` (1200×630) — the preview card: photo, name, one-line pitch, tags.
- **Important for future updates:** when replacing `index.html` with a new artifact export, keep this `<head>` block at the top and the GoatCounter lines at the bottom.

## 2026-11-19 — Page made small enough for LinkedIn
- **Branch:** `shrink-page` (merge into `main` only after Daryl approves)
- **Why:** LinkedIn Post Inspector refused to read the page: "larger than our threshold, maximum 3,145,728 bytes". The page was ~4.5 MB because every screenshot was embedded inside the HTML.
- **Changed:** all 37 images moved out of `index.html` into `images/` as separate files; `index.html` is now ~90 KB. Images load lazily as you scroll. Nothing looks different.
- **New build process (use this for every future update):**
  1. Export the latest Claude artifact to `tools/artifact-export.html` (not committed; it's in `.gitignore`).
  2. Run `python3 tools/build.py tools/artifact-export.html`. It extracts images into `images/`, removes unused ones, adds the `<head>` from `tools/head.html` (title, preview tags, base styles) and the GoatCounter script from `tools/tail.html`, and prints what it did.
  3. Commit on a new branch, open a pull request, and merge only after Daryl approves.

## 2026-11-20: Credit Heycars for its growth
- Branch: fix/credit-heycars-growth
- Why: Heycars' growth (~500 to ~400k monthly requests) was Heycars' doing; Daryl supported the pivot. Approved by Daryl 16:37 SGT.
- Changes: case title and index entry now "Supporting Heycars' pivot to resell Splyt's supply"; facts strip label now "Heycars' monthly requests, after a pivot I supported". Outcome text already credited Heycars.
- Build: python3 tools/build.py tools/artifact-export.html (37 images, index.html 0.09 MB)
- Claude artifact updated to v76 in the same change.
