
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

General Usage

Q: What does the Free Tier include?
The Free Tier includes up to 10,000 uploaded images, 1,000 hosted inference API calls per month, and full access to core features like annotation, model training, export, and workflows.

Q: What are credits and how are they used?
Credits are used for tasks like training models, creating new dataset versions, and exporting models. One credit typically equals 30 minutes of GPU training time.

Q: When do credits reset?
Credits and hosted inference calls reset monthly.
Annotation and Dataset Management

Q: Can I annotate images manually on the Free Tier?
Yes, manual annotation is available on all plans, including the Free Tier.

Q: Why are some images not uploading?
Roboflow may block near-duplicate images from uploading. Try renaming or adjusting the images if needed.
Model Training

Q: Can I fine-tune a model on the Free Tier?
Yes, but fine-tuning uses credits. The number of credits required depends on the training time and dataset size.

Q: Can I train a model from a Roboflow Universe dataset?
Yes, you can clone datasets from Universe and train them as your own project.
Export and Download

Q: Can I export a trained model on the Free Tier?
Yes, but exporting uses credits. The number of credits depends on the model type and export format.

Q: Why can’t I export my dataset?
If you’ve exceeded your generated image limit (from augmentations or multiple versions), you may need to delete extra versions to free up space.

Q: Can I download my source images and annotations without exporting?
Yes, as long as you’re under your image limit. If export is blocked, it's likely due to augmented/generated images.
Deployment and Inference

Q: How many inference calls do I get on the Free Tier?
You get 1,000 hosted inference API calls per month, per workspace.

Q: Do self-hosted deployments count against usage?
Yes. Whether hosted by Roboflow or self-hosted, API calls and video inference still count toward your usage limits.

Q: Can I deploy to devices like Jetson or Luxonis?
Yes, Roboflow provides deployment options for edge devices that do not count against hosted API usage.
Research and Credit Increases

Q: I'm a student or researcher and need more credits. What can I do?
You can apply for additional credits and support here: https://roboflow.com/contribute
Troubleshooting and Support

Q: Where can I monitor my usage?
Go to your Workspace > Settings > Usage to see your current credits, API calls, and generated images.

Q: Where do I get help if I'm stuck?
Post a question on the Roboflow Forum. Include screenshots, error messages, and a description of the issue for faster help.





what i learned and what the format for the txt file should be for the images.
corresponds to an image (same filename) and contains bounding box annotations for that image. It's how YOLO knows where the object is and what class it belongs to.
[class_id] [x_center] [y_center] [width] [height]
