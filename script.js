document.getElementById("fetch-article").addEventListener("click", async () => {
    const articleContainer = document.getElementById("article-container");
    const titleElement = document.getElementById("article-title");
    const summaryElement = document.getElementById("article-summary");
    const linkElement = document.getElementById("article-link");

    titleElement.textContent = "Loading...";
    summaryElement.textContent = "";
    linkElement.style.display = "none";

    try {
        const response = await fetch("https://en.wikipedia.org/api/rest_v1/page/random/summary");
        if (response.ok) {
            const data = await response.json();
            const { title, extract, content_urls } = data;

            titleElement.textContent = title;
            summaryElement.textContent = extract;
            linkElement.href = content_urls.desktop.page;
            linkElement.style.display = "inline-block";
            linkElement.textContent = "Read Full Article";
        } else {
            titleElement.textContent = "Error fetching article.";
        }
    } catch (error) {
        titleElement.textContent = "Error fetching article.";
        console.error(error);
    }
});

// hamburger 
// Toggle the mobile menu
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');

hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('active');
});


