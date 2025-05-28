document.addEventListener("DOMContentLoaded", function () {
  const topicInput = document.getElementById("topicInput");
  const searchBtn = document.getElementById("searchBtn");
  const maxResults = document.getElementById("maxResults");
  const tagsContainer = document.getElementById("tagsContainer");
  const sourceInfo = document.getElementById("sourceInfo");
  const copyBtn = document.getElementById("copyBtn");
  const toggleBtn = document.getElementById("toggleCheck");

  // Initialize with empty state
  initializeEmptyState();

  //Adding event to the toggle btn
  toggleBtn.addEventListener("click", changeMode);
  //Toggle for light/dark mode
  function changeMode() {
    //getting root
    const root = document.documentElement;

    const youtubeDark = getComputedStyle(root)
      .getPropertyValue("--youtube-dark")
      .trim();
    //validating youtubeDark variable and change the mode according to that
    if (youtubeDark == "#282828") {
      root.style.setProperty("--youtube-dark", "white");
      root.style.setProperty("--youtube-light", "#181818");
      root.style.setProperty("--tag-color", "#2c2c2c");
      root.style.setProperty("--tag-hover", "#3a3a3a");
      root.style.setProperty("--container-color", "black");
      document.getElementById("topicInput").style.backgroundColor =
        "transparent";
      document.getElementById("maxResults").style.backgroundColor =
        "transparent";
      document.getElementById("maxResults").style.color = "white";

      document.getElementById("topicInput").style.color = "white";
      document.getElementById("copyBtn").style.border = "1px solid white";
    } else {
      root.style.setProperty("--youtube-dark", "#282828");
      root.style.setProperty("--youtube-light", "white");
      root.style.setProperty("--tag-color", "#f1f1f1");
      root.style.setProperty("--tag-hover", "#e5e5e5");
      root.style.setProperty("--container-color", "white");
      document.getElementById("topicInput").style.backgroundColor =
        "transparent";
      document.getElementById("maxResults").style.backgroundColor =
        "transparent";
      document.getElementById("maxResults").style.color = "black";

      document.getElementById("topicInput").style.color = "black";
      document.getElementById("copyBtn").style.border = "1px solid white";
    }
  }

  searchBtn.addEventListener("click", fetchTags);
  topicInput.addEventListener("keypress", function (e) {
    if (e.key === "Enter") fetchTags();
  });

  copyBtn.addEventListener("click", copyAllTags);

  function fetchTags() {
    const topic = topicInput.value.trim();
    const maxTags = maxResults.value;

    if (!topic) {
      showError("Please enter a topic");
      return;
    }

    // Show loading state
    showLoadingState();

    fetch("/get_tags", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: `topic=${encodeURIComponent(topic)}&max_results=${maxTags}`,
    })
      .then(handleResponse)
      .then((data) => {
        if (data.error) {
          showError(data.error);
        } else {
          displayTags(data.tags, data.source);
        }
      })
      .catch(handleError);
  }

  function handleResponse(response) {
    if (!response.ok) {
      throw new Error(`API request failed with status ${response.status}`);
    }
    return response.json();
  }

  function displayTags(tags, source) {
    tagsContainer.innerHTML = "";

    if (!tags || tags.length === 0) {
      showError("No tags found for this topic. Try a different search term.");
      return;
    }

    // Show source info
    sourceInfo.textContent = `Tags sourced from: ${source}`;

    // Display tags
    tags.forEach((tag) => {
      createTagElement(tag);
    });

    // Show copy button
    copyBtn.classList.remove("hidden");
  }

  function createTagElement(tagText) {
    const tagElement = document.createElement("div");
    tagElement.className = "tag";
    tagElement.textContent = tagText;
    tagElement.title = "Click to copy";

    tagElement.addEventListener("click", function () {
      copyToClipboard(tagText);
      showCopiedFeedback(tagElement);
    });

    tagsContainer.appendChild(tagElement);
  }

  function copyAllTags() {
    const tags = Array.from(document.querySelectorAll(".tag"))
      .map((tag) => tag.textContent)
      .join(", ");

    copyToClipboard(tags);
    showCopiedFeedback(copyBtn, '<i class="fas fa-check"></i> Copied!');
  }

  function copyToClipboard(text) {
    navigator.clipboard.writeText(text).catch((err) => {
      console.error("Could not copy text: ", err);
    });
  }

  function showCopiedFeedback(element, temporaryText = "Copied!") {
    const originalText = element.innerHTML;
    element.innerHTML = temporaryText;

    setTimeout(() => {
      element.innerHTML = originalText;
    }, 1500);
  }

  function showLoadingState() {
    tagsContainer.innerHTML = '<div class="loading"></div>';
    sourceInfo.textContent = "Loading...";
    copyBtn.classList.add("hidden");
  }

  function showError(message) {
    tagsContainer.innerHTML = `
            <div class="error-message">
                <i class="fas fa-exclamation-circle"></i> ${message}
            </div>
        `;
    sourceInfo.textContent = "";
    copyBtn.classList.add("hidden");
  }

  function handleError(error) {
    console.error("Error:", error);
    showError("Failed to load tags. Please try again later.");
  }

  function initializeEmptyState() {
    tagsContainer.innerHTML = `
            <div class="placeholder">
                <i class="fab fa-youtube"></i>
                <p>Enter a topic to generate YouTube tags</p>
            </div>
        `;
    sourceInfo.textContent = "";
    copyBtn.classList.add("hidden");
  }
});
