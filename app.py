from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
API_VERSION = "1.0.0"


def get_all_marketplace():
    return [
        {
            "id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
            "name": "Green Planet",
            "projectType": "Forest",
            "offsetGoalCO2": 100532,
            "imageUrl": "static/project-1.jpg",
            "geoLocation": {
                "lattitude": -0.228021,
                "longitude": 15.8276587
            },
            "country": "Congo",
            "ce2PPT": 12.8,
            "currency": "EUR",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "offsetingPartner": {
                "name": "Southpole (c)",
                "homePage": "https://www.southpole.com"
            }
        },
        {
            "id": "d290f1ee-6c54-4b01-90e6-d701748f0852",
            "name": "Amazonia Project",
            "projectType": "Forest",
            "offsetGoalCO2": 90532,
            "imageUrl": "static/project-2.jpg",
            "geoLocation": {
                "lattitude": -3.4653,
                "longitude": -62.2159
            },
            "country": "Brazil",
            "ce2PPT": 20.8,
            "currency": "EUR",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "offsetingPartner": {
                "name": "Southpole (c)",
                "homePage": "https://www.southpole.com"
            }
        },
        {
            "id": "d290f1ee-6c54-4b01-90e6-d701748f0853",
            "name": "Tree Friends",
            "projectType": "Forest",
            "offsetGoalCO2": 90532,
            "imageUrl": "static/project-3.jpg",
            "geoLocation": {
                "lattitude": 12.8654,
                "longitude": -85.2072
            },
            "country": "Nicaragua",
            "ce2PPT": 15.25,
            "currency": "EUR",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "offsetingPartner": {
                "name": "Southpole (c)",
                "homePage": "https://www.southpole.com"
            }
        }
    ]


def get_marketplace(project_id):
    return get_all_marketplace()[0]


def get_company_dashboard(company_id):
    return {
        "totalEmissions": 48,
        "totalChange": -7.6,
        "elements": [
            {
                "label": "Transportation",
                "emmisions": 29,
                "change": -7.6
            }
        ]
    }


@app.route("/{}/marketplace/project".format(API_VERSION))
def marketplace():
    return jsonify(get_all_marketplace())


@app.route("/{}/marketplace/project/<project_id>".format(API_VERSION))
def marketplace_detail(project_id):
    return jsonify(get_marketplace(project_id))


@app.route("/{}/company/<company_id>/dashboard".format(API_VERSION))
def company_dashboard(company_id):
    return jsonify(get_company_dashboard(company_id))
