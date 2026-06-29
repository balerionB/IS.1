"""
==========================================
Analytics Service
Contains all Business Intelligence queries.
==========================================
"""

from models.service_request import ServiceRequest


class AnalyticsService:

    @staticmethod
    def get_summary():

        return {

            "total_requests": 5241,

            "resolved": 4928,

            "pending": 313,

            "average_sla": "2.3 Days",

            "satisfaction": "94%"

        }

    @staticmethod
    def get_monthly_requests():
        return {

            "labels": [

                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun"

            ],

            "values": [

                112,
                145,
                168,
                190,
                214,
                236

            ]

        }


@staticmethod
def department_performance():
    return {

        "labels": [

            "Roads",

            "Water",

            "Health",

            "ICT",

            "Finance"

        ],

        "values": [

            94,

            88,

            91,

            86,

            96

        ]

    }
@staticmethod
def category_breakdown():

    return {

        "labels":[

            "Roads",

            "Water",

            "Garbage",

            "Permits",

            "Lighting"

        ],

        "values":[

            130,

            96,

            65,

            88,

            42

        ]

    }
@staticmethod
def sla_compliance():

    return {

        "completed":96,

        "late":4

    }
@staticmethod
def officer_productivity():

    return{

        "labels":[

            "James",

            "Anne",

            "Peter",

            "Lucy",

            "John"

        ],

        "values":[

            120,

            111,

            96,

            91,

            87

        ]

    }
@staticmethod
def generate_report():

    return {

        "summary":{

            "total":5241,

            "resolved":4928,

            "pending":313,

            "sla":"97%"

        },

        "departments":[

            {

                "name":"Roads",

                "requests":1124

            },

            {

                "name":"Water",

                "requests":892

            },

            {

                "name":"Health",

                "requests":781

            }

        ]

    }
@staticmethod

def executive_insights():

    return [

        "Road requests increased by 14% this month.",

        "Water backlog has reduced by 8%.",

        "Health achieved 98% SLA compliance.",

        "ICT processed the most requests."

    ]