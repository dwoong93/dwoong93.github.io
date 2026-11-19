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
