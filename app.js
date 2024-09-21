const express = require('express');
const fetch = (...args) =>
    import('node-fetch').then(({ default: fetch }) => fetch(...args));
const app = express();
const PORT = 3000;

// Regex to validate a URL
const isValidUrl = (string) => {
    try {
        new URL(string);
        return true;
    } catch (_) {
        return false;  
    }
};

app.use(express.static('public'));

app.get('/search', async (req, res) => {
    const query = req.query.q;

    let fetchUrl = '';

    if (isValidUrl(query)) {
        fetchUrl = query; // Use the provided URL directly
    } else {
        // For non-URLs, redirect to a search engine (like Google)
        fetchUrl = `https://www.google.com/search?q=${encodeURIComponent(query)}`;
    }

    try {
        const response = await fetch(fetchUrl, { method: 'GET', headers: { 'User-Agent': 'Mozilla/5.0' } });
        const contentType = response.headers.get('content-type');

        if (!contentType || !contentType.includes('text/html')) {
            return res.status(400).send('URL does not return HTML.');
        }

        let body = await response.text();
        
        // Base URL for resolving relative paths
        const baseUrl = new URL(fetchUrl).origin;

        // Rewrite URLs for resources
        body = body.replace(/(href|src)=["']([^"']+)["']/g, (match, attr, url) => {
            const fullUrl = url.startsWith('http') ? url : `${baseUrl}/${url}`;
            return `${attr}="${fullUrl}"`;
        });

        // Make sure to include Google scripts and styles
        body = body.replace(/<head>/, `<head><base href="${baseUrl}">`);

        res.send(body);
    } catch (error) {
        console.error('Error fetching URL:', error);
        res.status(500).send('Error fetching URL');
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
