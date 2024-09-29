let currentIndex = -1;  // Start with an invalid index
let loadTimeout;  // Variable to store the timeout

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
    iframe.src = formatURL(data[currentIndex].Website);

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
    updateIframe();  // Load the first random company when the page loads
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
