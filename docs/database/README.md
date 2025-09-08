<h1 style="font-size: 48px">verdant database</h1>

## Technologies
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

## Info: 
Database stored in MongoDB Atlas Cluster, total  logical size of 137mb and 24,455 pages indexed</h2>

```json
{
  "_id": {
    "$oid": "689b48feb5f350176a0edba0"
  },
  "url": "https://www.merriam-webster.com/dictionary/verdant",
  "description": "English speakers have used verdant as a synonym for green since at least the 16th century, and...",
  "frequency_dict": {
    "with": 1,
    "Remarkable": 1,
    "Origins": 1,
    "Games": 1,
    "Quizzes": 1,
    "Learn": 1,
    "new": 1,
    ...
  },
  "title": "VERDANT Definition & Meaning\n"
}

```
Upon user request, 500 most relevant pages get returned to backend as MongoDB uses a faster c++ sorting algorithm for more direct relationship, while the verdant backend has a more complex algorithm to filter results into 10 most relevant.  
