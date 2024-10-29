let currentIndex = -1;  // Start with an invalid index
let loadTimeout;  // Variable to store the timeout
let data = [];  // Array to hold the URLs from sites.txt

// Function to fetch URLs from the sites.txt file
function loadSites() {
    fetch("sites.txt")
        .then(response => response.text())
        .then(text => {
            // Split the file contents by new lines to get each URL
            data = text.split("\n").map(url => url.trim()).filter(url => url);
            if (data.length > 0) {
                updateIframe();  // Load the first random company after loading URLs
            } else {
                console.error("No URLs found in sites.txt");
            }
        })
        .catch(error => console.error("Error loading sites:", error));
}

function formatURL(url) {
    if (!url.startsWith("http://") && !url.startsWith("https://")) {
        return "https://" + url;
    }
    return url;
}

function updateIframe() {
    // Generate a random index
    currentIndex = Math.floor(Math.random() * data.length);
    const iframe = document.getElementById("embedded-frame");
    iframe.src = formatURL(data[currentIndex]);

    // Set a timeout to check for loading issues
    loadTimeout = setTimeout(() => {
        console.log("Loading timeout. Skipping to the next website.");
        skipToNext();
    }, 5000);  // 5 seconds timeout
}

function openInNewTab() {
    const iframe = document.getElementById("embedded-frame");
    const url = iframe.src;
    if (url) {
        window.open(url, "_blank");
    } else {
        alert("No website loaded to open.");
    }
}

function skipToNext() {
    // Generate a new random index
    currentIndex = Math.floor(Math.random() * data.length);
    updateIframe();
}

function closeBanner() {
    document.getElementById('banner').style.display = 'none';
}

window.onload = function() {
    loadSites();  // Load URLs from sites.txt when the page loads
};

const iframe = document.getElementById("embedded-frame");
iframe.onload = function() {
    console.log("Website loaded successfully.");
    clearTimeout(loadTimeout);  // Clear the timeout if loaded successfully
};

iframe.onerror = function() {
    console.log("Error loading website, skipping to the next one...");
    skipToNext();
};
