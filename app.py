# ''''''

# from flask import Flask, request, Response, redirect
# import requests

# app = Flask(__name__)

# # Route for the home page
# @app.route('/')
# def home():
#     return '''
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta http-equiv="X-UA-Compatible" content="IE=edge">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Google Search Proxy</title>
#     </head>
#     <body>
#         <!-- Search Form -->
#         <form id="searchForm">
#             <input type="text" name="q" placeholder="Search Google">
#             <button type="submit">Search</button>
#         </form>

#         <!-- Iframe to display search results -->
#         <iframe id="searchFrame" width="100%" height="600px"></iframe>

#         <script>
#             const form = document.getElementById('searchForm');
#             const iframe = document.getElementById('searchFrame');

#             form.onsubmit = (e) => {
#                 e.preventDefault();
#                 const query = form.querySelector('input[name="q"]').value;
#                 iframe.src = `/proxy_search?q=${encodeURIComponent(query)}`;
#             };

#             iframe.onload = function() {
#                 const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
#                 const links = iframeDoc.querySelectorAll('a');

#                 links.forEach(link => {
#                     link.onclick = function(e) {
#                         e.preventDefault();
#                         const url = link.getAttribute('href');
#                         if (url.startsWith('http')) {
#                             iframe.src = `/proxy_url?url=${encodeURIComponent(url)}`;
#                         }
#                     };
#                 });
#             };
#         </script>
#     </body>
#     </html>
#     '''

# # Route for the Google search proxy
# @app.route('/proxy_search')
# def proxy_search():
#     query = request.args.get('q')
#     if not query:
#         return "No query provided", 400

#     google_url = f'https://www.google.com/search?q={query}'
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
#     }

#     try:
#         response = requests.get(google_url, headers=headers)
#         return Response(response.content, content_type=response.headers['Content-Type'])
#     except requests.exceptions.RequestException as e:
#         return f"Error fetching search results: {e}", 500

# # Route for proxying external URLs
# @app.route('/proxy_url')
# def proxy_url():
#     url = request.args.get('url')
#     if not url:
#         return "No URL provided", 400

#     # Fetch the content of the external URL
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
#     }

#     try:
#         response = requests.get(url, headers=headers)
#         return Response(response.content, content_type=response.headers['Content-Type'])
#     except requests.exceptions.RequestException as e:
#         return f"Error fetching the requested URL: {e}", 500

# if __name__ == '__main__':
#     app.run(debug=True)
# ''''''