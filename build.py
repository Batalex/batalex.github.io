"""Minimal python build script from
https://staticjinja.readthedocs.io/en/stable/user/advanced.html#using-custom-build-scripts
"""

from staticjinja import Site

SITENAME = "Alex Batisse"
DEFAULT_LANG = "en"
links = [
    {
        "href": "https://github.com/batalex",
        "text": "GitHub",
        "path_d": "M12 2C6.475 2 2 6.588 2 12.253c0 4.537 2.862 8.369 6.838 9.727.5.09.687-.218.687-.487 0-.243-.013-1.05-.013-1.91C7 20.059 6.35 18.957 6.15 18.38c-.113-.295-.6-1.205-1.025-1.448-.35-.192-.85-.667-.013-.68.788-.012 1.35.744 1.538 1.051.9 1.551 2.338 1.116 2.912.846.088-.666.35-1.115.638-1.371-2.225-.256-4.55-1.14-4.55-5.062 0-1.115.387-2.038 1.025-2.756-.1-.256-.45-1.307.1-2.717 0 0 .837-.269 2.75 1.051.8-.23 1.65-.346 2.5-.346.85 0 1.7.115 2.5.346 1.912-1.333 2.75-1.05 2.75-1.05.55 1.409.2 2.46.1 2.716.637.718 1.025 1.628 1.025 2.756 0 3.934-2.337 4.806-4.562 5.062.362.32.675.936.675 1.897 0 1.371-.013 2.473-.013 2.82 0 .268.188.589.688.486a10.039 10.039 0 0 0 4.932-3.74A10.447 10.447 0 0 0 22 12.253C22 6.588 17.525 2 12 2Z",
        "vbox": "0 0 24 24",
    },
    {
        "href": "https://gitlab.com/abatisse",
        "text": "GitLab",
        "path_d": "M282.83,170.73l-.27-.69-26.14-68.22a6.81,6.81,0,0,0-2.69-3.24,7,7,0,0,0-8,.43,7,7,0,0,0-2.32,3.52l-17.65,54H154.29l-17.65-54A6.86,6.86,0,0,0,134.32,99a7,7,0,0,0-8-.43,6.87,6.87,0,0,0-2.69,3.24L97.44,170l-.26.69a48.54,48.54,0,0,0,16.1,56.1l.09.07.24.17,39.82,29.82,19.7,14.91,12,9.06a8.07,8.07,0,0,0,9.76,0l12-9.06,19.7-14.91,40.06-30,.1-.08A48.56,48.56,0,0,0,282.83,170.73Z",
        "vbox": "0 0 380 380",
    },
    {
        "href": "https://www.linkedin.com/in/alexandre-batisse-401578b4/",
        "text": "LinkedIn",
        "path_d": "M18.335 18.339H15.67v-4.177c0-.996-.02-2.278-1.39-2.278-1.389 0-1.601 1.084-1.601 2.205v4.25h-2.666V9.75h2.56v1.17h.035c.358-.674 1.228-1.387 2.528-1.387 2.7 0 3.2 1.778 3.2 4.091v4.715zM7.003 8.575a1.546 1.546 0 01-1.548-1.549 1.548 1.548 0 111.547 1.549zm1.336 9.764H5.666V9.75H8.34v8.589zM19.67 3H4.329C3.593 3 3 3.58 3 4.297v15.406C3 20.42 3.594 21 4.328 21h15.338C20.4 21 21 20.42 21 19.703V4.297C21 3.58 20.4 3 19.666 3h.003z",
        "vbox": "0 0 24 24",
    },
]

mail = {
    "mail": "alexandre.batisse@hey.com",
    "path_d": "M1.5 8.67v8.58a3 3 0 0 0 3 3h15a3 3 0 0 0 3-3V8.67l-8.928 5.493a3 3 0 0 1-3.144 0L1.5 8.67Z",
    "path_d2": "M22.5 6.908V6.75a3 3 0 0 0-3-3h-15a3 3 0 0 0-3 3v.158l9.714 5.978a1.5 1.5 0 0 0 1.572 0L22.5 6.908Z",
    "vbox": "0 0 24 24",
}

timeline = [
    {
        "firm": "Canonical",
        "location": "Remote",
        "startDate": "2024",
        "endDate": None,
        "title": "Software Engineer",
        "subPhases": [
            {
                "title": "Software Engineer - Data Platform",
                "content": "I am part of the Big Data team, where I work on charmed operators to provide distributed system management to open source technologies.",
                "startDate": "fev. 2024",
            },
        ],
    },
    {
        "firm": "HEVA",
        "location": "Lyon (FR)",
        "startDate": "2019",
        "endDate": "2024",
        "title": "Data Scientist",
        "subPhases": [
            {
                "title": "Data Scientist & Tech lead",
                "content": "I took on some additional responsibilities. I provided technical support for the entire firm and managed the evolution of our technical stack.",
                "startDate": "Nov. 2020",
            },
            {
                "title": "Data Scientist",
                "content": "My responsibilities were twofold. First, I conducted our clients' (pharmaceutical industry) studies on national health claim data. This work involved data management, statistical modeling, and reporting with the PyData stack. Secondly, I tended to my team's internal tools as a maintainer and Python developer.",
                "startDate": "Jan. 2019",
            },
        ],
    },
    {
        "firm": "Worldline",
        "location": "Lyon (FR)",
        "startDate": "2017",
        "endDate": "2018",
        "title": "Software Engineer",
        "subPhases": [
            {
                "title": "Software Engineer",
                "content": "I was part of the Business Intelligence & Big Data team in charge of designing and building a production-ready data science platform for training and deploying models. I worked on several projects involving banking information (fraud detection, cheque recovery prediction) with full-fledged data scientists.",
                "startDate": "Jan. 2017",
            },
            {
                "title": "Engineering internship",
                "content": "I worked in the Business Development unit on a banking chatbot.\n",
                "startDate": "Jan. 2017",
            },
        ],
    },
]

projects = [
    {
        "title": "pyOpenSci editor",
        "content": "I am proud to have joined the community that supports free and open Python tools for processing scientific data.",
        "link": "https://pyopensci.org",
        "short": "pyopensci.org",
        "illustration": "✔",
    },
    {
        "title": "Twitter campaign",
        "content": "I co-created a bot for a music promotional campaign. Over five days, the bot generated and served over 4,000 short videos and were among the top trending topics worldwide.",
        "link": "https://twitter.com/hacklazzcc",
        "short": "twitter.com",
        "illustration": "🤖",
    },
    {
        "title": "Effective Pandas Book",
        "content": "I am honored to be credited as a technical editor in this excellent book by Matt Harrison. This book presents the best practices for manipulating data with Pandas.",
        "link": "https://store.metasnake.com/effective-pandas-book",
        "short": "metasnake.com",
        "illustration": "📕",
    },
    {
        "title": "Camelia",
        "content": "I co-created Camelia, a platform combining audio analysis, video generation, and background workers to allow music artists to create videos quickly.",
        "link": "https://www.camelia.studio/",
        "short": "camelia.studio",
        "illustration": "🎵",
    },
    {
        "title": "Personal website",
        "content": "This personal website was the perfect opportunity to take a shot at some technologies I do not usually use",
        "short": "",
        "link": "#",
        "illustration": "🖼️",
    },
    {
        "title": "Scikit-learn Sprint of the Decade",
        "content": "I participated in a 3-days scikit-learn sprint in Jan. 2020. I met some lovely people there and contributed to one of the most essential packages in the PyData ecosystem.",
        "link": "https://scikit-learn.fondation-inria.fr/paris-sprint-of-the-decade-happy-birthday-scikit-learn/",
        "short": "scikit-learn.fondation-inria.fr",
        "illustration": "👨‍💻",
    },
]
site = Site.make_site(
    env_globals=dict(locals()) | {"greetings": "Hello"}, outpath="output"
)
# diable automatic reloading
site.render(use_reloader=False)
