<h1 style="font-size: 48px">verdant backend</h1>

## Technologies
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PythonAnywhere](https://img.shields.io/badge/PythonAnywhere-1D9FD7?style=for-the-badge&logo=python&logoColor=white)



## Steps
<h4>1.) User submits a POST request containing their search query to rasberry pi running a FastAPI REST API and Postgres + pgvector DB, with cloudflare tunnels as a reverse proxy. ) </h4>


<h4>2.) The API then queries the database and fetches the 50 most similar chunks based on cosine similarity. )</h4>

<h4>3.) The sites are each given a score based on the formula below:</h4>

<img style="width: 100%; height: auto;" src="../../images/BackendEq.png">

<h5>Note: The formula gives the highest results to sites with a higher % of the most search queries, giving a bonus to sites that have search queries in the URL text.</h5>

<h4>4.) Finally, the backend returns the most relevant sites, and a corresponding match score for the highest match, ranging from 0-100%</h4>
