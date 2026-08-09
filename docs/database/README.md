<h1 style="font-size: 48px">verdant database</h1>

## Technologies
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

## Info: 
Database stored in Postgres hosted locally on Rasberry Pi, with cloudflare tunnels as a reverse proxy.</h2>

```json
{
  "id": 384217,
  "url": "https://www.merriam-webster.com/dictionary/verdant",
  "title": "Verdant Definition & Meaning - Merriam-Webster",
  "author": null,
  "chunk": "verdant adjective. 1: green with growing plants. 2: of the color green. The hills were lush and verdant after the spring rains. ...",
  "embedding": [
    0.0124,
    -0.0837,
    0.0412,
    0.1179,
    -0.0291,
    0.0648,
    0.0037,
    "...",
    0.0216
  ]
}

```
Upon user request, the top 50 most relevant chunks are found using pgvector cosine-similarity. Each unique site is send to the backend, reordered, and displayed on the frontend.
