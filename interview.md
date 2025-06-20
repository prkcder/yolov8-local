
While exploring the Roboflow forum, I noticed a UI issue where the page title overlaps with the navigation bar when scrolling. I dug into the CSS and structure and realized the title and nav bar are styled as separate fixed elements without coordination on scroll. My suggestion would be to dynamically adjust the layout so that when a user scrolls, the title shrinks and smoothly merges into the navbar, rather than pushing against it. This could be done by using a scroll listener to toggle a class that modifies padding, font size, and layout via flexbox—keeping the header compact and functional without overlap.

/* NAVBAR: logo + links + auth buttons all in one row */
#rf-navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;                /* Allows wrapping on smaller screens */
  padding: 0.75rem 1.5rem;
  background: white;
  z-index: 10;
  position: sticky;
  top: 0;
  box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}

/* Group logo and links together */
.nav-left {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

/* Nav links container */
.rf-nav-link-container {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

/* Auth buttons aligned right */
.auth-buttons {
  display: flex;
  gap: 0.5rem;
  align-items: center;
  flex-shrink: 0;
}

/* Prevent layout bugs from title */
.d-header {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  height: auto !important;       /* Allow expansion */
  min-height: 4rem;
  padding: 0 1.5rem;
  overflow: visible !important;
  background: white;
}

/* Allow header title to wrap under nav */
.header-title {
  word-break: break-word;
  white-space: normal;
  font-size: 1.25rem;
  margin-top: 0.5rem;
}



## Roboflow Free Tier Observations
- Max 1 Workspace per account (hard stop)
- Training credits: 1,000 (resets every 2 weeks)
- No Monitoring or Production Deployment UI
- Hosted Inference via API still available after training
 UX Opportunity Example:
 “Workspace cancellation button hard to locate on ultra-wide monitor; contrast is too low on white. Could benefit from a more prominent design pattern (e.g., red text link or tooltip explanation).”

## UX Friction Points
1. Workspace Deletion: Hard to find on wide screens, white text on white background.
2. Training Tab: Doesn’t show how many credits are consumed until the button is pressed.
3. Label Creation: No quick tutorial or AI auto-suggest for first-time users.


## Community Insights
- Users often confuse Roboflow Train vs. external training (YOLOv8, etc.)
- Many users hit the “Training credits depleted” issue and don’t know when it resets
- Some users try to use models with very few examples (<50) and get poor results


## Docs Gaps / Opportunities
- “Free Tier Limits” should be clearer in the UI and docs.
- Workspace restriction (1 per account) isn’t mentioned early in onboarding.
- Training cost calculator could be helpful before starting a job.





some FAQ I created based on the fourm
(check reddit and support engineer should go there as most users would usually go on reddit)

