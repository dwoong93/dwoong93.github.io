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
