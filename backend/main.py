from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
from math import log
from urllib.parse import urlparse
import json
from flask import Flask
from flask import request
from dotenv import load_dotenv
import os 

app = Flask(__name__)

MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASS = os.environ.get("MONGO_PASS")

@app.route("/verdant/api", methods=["POST"])
def return_websites():
    uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@verdant-db.lliw5at.mongodb.net/?retryWrites=true&w=majority&appName=Verdant-DB"
    client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where(), serverSelectionTimeoutMS=5000)
    connection = client['verdant_database']
    website_info = connection['Website info']

    queries = request.args.getlist("term")
    common_words = set(
        """
    a about above across after afterwards again against all almost alone along
    already also although always am among amongst amount an and another any anyhow
    anyone anything anyway anywhere are around as at

    back be became because become becomes becoming been before beforehand behind
    being below beside besides between beyond both bottom but by

    call can cannot ca could

    did do does doing done down due during

    each eight either eleven else elsewhere empty enough even ever every
    everyone everything everywhere except

    few fifteen fifty first five for former formerly forty four from front full
    further

    get give go

    had has have he hence her here hereafter hereby herein hereupon hers herself
    him himself his how however hundred

    i if in indeed into is it its itself

    keep

    last latter latterly least less

    just

    made make many may me meanwhile might mine more moreover most mostly move much
    must my myself

    name namely neither never nevertheless next nine no nobody none noone nor not
    nothing now nowhere

    of off often on once one only onto or other others otherwise our ours ourselves
    out over own

    part per perhaps please put

    quite

    rather re really regarding

    same say see seem seemed seeming seems serious several she should show side
    since six sixty so some somehow someone something sometime sometimes somewhere
    still such

    take ten than that the their them themselves then thence there thereafter
    thereby therefore therein thereupon these they third this those though three
    through throughout thru thus to together too top toward towards twelve twenty
    two

    under until up unless upon us used using

    various very very via was we well were what whatever when whence whenever where
    whereafter whereas whereby wherein whereupon wherever whether which while
    whither who whoever whole whom whose why will with within without would

    yet you your yours yourself yourselves
    """.split()
    )

    queries = [query for query in queries if query not in common_words]

    or_conditions = [{f"frequency_dict.{q}": {"$exists": True}} for q in queries]

    fields = {
        "url": 1,
        "title": 1,
        "description": 1,
        "frequency_dict": 1,
    }
    for term in queries:
        fields[f"{term}_count"] = f"$frequency_dict.{term}"

    items = list(website_info.find(
            {"$or": or_conditions},
        fields
    ).limit(500))


    website_list = []
    for website in items:
        terms_matched = 0
        website_output = {}
        sum = 0
        for item in queries:
            index = f"{item}_count"
            if index in website:
                terms_matched += website[index]



        length_penalty = log(len(website["frequency_dict"]) + 1)
        parsed_url = urlparse(website['url'])
        url_parts = parsed_url.netloc.split('.') + parsed_url.path.split('/')
        url_parts = [part.lower() for part in url_parts if part]




        url_matches = 0
        # Rewards search terms that appear in URLs
        for i in queries:
            if i in url_parts:
                url_matches += 1

        if terms_matched > 0:
            url_bonus = 1 + (2*url_matches)
        else:
            url_bonus = 0

        sum = (terms_matched / len(queries)) / (length_penalty/2)
        sum *= url_bonus**2


        # Adding website title to output
        try:
            output_title = website["title"][:47] + "..."
            website_output["title"] = output_title
        except:
            output_title = "Title Unknown"
            website_output["title"] = output_title

        # Adding website url
        website_output["url"] = website["url"]
        website_output["description"] = website["description"]
        website_output["score"] = sum

        website_list.append(website_output)



    sorted_list = sorted(website_list, key=lambda x: x["score"], reverse=True)
    match_score = 0
    websites_loaded_count = 0

    output_list = []
    websites_loaded = []
    try:
        if sorted_list[:1][0]["score"] != 0:
            possible_results = sorted_list[:10]
            for item in possible_results:
                if item["score"] > 0.25:
                    websites_loaded.append(item)
                    websites_loaded_count += 1
            match_score = sorted_list[:1][0]["score"] / 3
    except:
        print("Sorry, no results found!")

    if match_score > 1:
        match_score = 100
    else:
        match_score = round((match_score*100), 2)

    output_list.append(match_score)
    output_list.append(websites_loaded_count)
    output_list.append(websites_loaded)

    print(output_list)
    api_output = {
        "match_score": output_list[0],
        "websites_loaded": output_list[1],
        "websites": output_list[2]
    }

    api_output_json = json.dumps(api_output, indent=4)
    return api_output_json