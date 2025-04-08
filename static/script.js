let currentIndex = -1;  // Start with an invalid index
let loadTimeout;  // Variable to store the timeout
let data = [];  // Array to hold the URLs from sites.txt

function formatURL(url) {
    if (!url.startsWith("http://") && !url.startsWith("https://")) {
        return "https://" + url;
    }
    return url;
}

function updateIframe() {
    // Generate a random index
    currentIndex = Math.floor(Math.random() * data.length);
    const url = formatURL(data[currentIndex].Website);
    const iframe = document.getElementById("embedded-frame");

    // Try to load the site
    try {
        iframe.src = url;
        
        // Add error handler for X-Frame-Options issues
        iframe.onerror = function() {
            console.log("Website blocked iframe loading, opening in new tab...");
            window.open(url, '_blank');
            // Load next site in iframe
            skipToNext();
        };

    } catch (error) {
        console.log("Error loading website:", error);
        window.open(url, '_blank');
        skipToNext();
    }

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
    clearTimeout(loadTimeout); // Clear any existing timeout
    // Generate a new random index
    currentIndex = Math.floor(Math.random() * data.length);
    updateIframe();
}

function closeBanner() {
    document.getElementById('banner').style.display = 'none';
}

// Add a message about sites opening in new tabs
function addNewTabMessage() {
    const banner = document.getElementById('banner');
    const message = document.createElement('div');
    message.className = 'subtitle';
    message.style.color = '#a4a4a4';
    message.style.fontSize = '12px';
    message.textContent = 'Note: Some sites may open in a new tab due to security settings';
    banner.appendChild(message);
}

window.onload = function() {
    // Fetch the company URLs from the static JSON file
    fetch('static/data.json')
        .then(response => response.json())
        .then(jsonData => {
            data = jsonData;
            updateIframe();  // Load the first random company when the data is loaded
            addNewTabMessage(); // Add the new tab message
        })
        .catch(error => {
            console.error('Error loading data:', error);
        });
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
