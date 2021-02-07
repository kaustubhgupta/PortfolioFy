from functions.addBlogs import addBlogsEntryL2
from functions.addHackathon import addHackathonEntryL2
from functions.addResume import addResumeEntryL2
from functions.addFooter import footer
from distutils.util import strtobool


def genHTMLLevel2(user_data, project_repos, hackathon_repos, blogs, stats_choice, social_links, resume_link, allow_footer):

    req_css = '''
    .h2-repo {
            font-size: xx-large;
            text-transform: none;

        }

        .h2-blog {
            text-transform: none;
            font-size: x-large;
        }

        .button {
            background-color: #d7e8f8;
            border: none;
            color: #0366d6;
            padding: 2px 6px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 16px;

        }
    '''

    template = f'''
    <html lang="en">

    <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <title>{user_data['name']} Portfolio</title>

    
    <script src="https://use.fontawesome.com/releases/v5.15.1/js/all.js" crossorigin="anonymous"></script>
   
    <link href="https://fonts.googleapis.com/css?family=Saira+Extra+Condensed:500,700" rel="stylesheet"
    type="text/css" />
    <link href="https://fonts.googleapis.com/css?family=Muli:400,400i,800,800i" rel="stylesheet" type="text/css" />
    
    <link href="https://kaustubhgupta.github.io/themescss/level2.css" rel="stylesheet" />
    <style>
    {req_css}
    </style>
    </head>

    <body id="page-top">
    <!-- Navigation-->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top" id="sideNav">
    <a class="navbar-brand js-scroll-trigger" href="#page-top">
    <span class="d-block d-lg-none">{user_data['name']}</span>

    <span class="d-none d-lg-block"><img class="img-fluid img-profile rounded-circle mx-auto mb-2"
    src="{user_data['git_photo_url']}" /></span>

    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
    aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span
    class="navbar-toggler-icon"></span></button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav">
    <li class="nav-item"><a class="nav-link js-scroll-trigger" href="#about">About</a></li>
    <li class="nav-item"><a class="nav-link js-scroll-trigger" href="#gitHubstats">GitHub Stats</a></li>
    <li class="nav-item"><a class="nav-link js-scroll-trigger" href="#projects">Projects</a></li>
    <!-- HACKATHON-NAV-ENTRY -->
    <!-- BLOGS-NAV-ENTRY -->
    </ul>
    </div>
    </nav>
    <!-- Page Content-->
    <div class="container-fluid p-0">
    <!-- About-->
    <section class="resume-section" id="about">
    <div class="resume-section-content">
    <h1 class="mb-0">
    {user_data['name']} 👨‍🎓
    </h1> 
    <br>
    <h3><span class="text-secondary">{user_data['git_bio']}</span></h3>
    <span class="text-info">Contact on Email: {user_data['git_email']}</span><br>
    <span class="text-primary">Followers: Followers: {user_data['git_followers']}, Following: {user_data['git_following']}</span>
    <br>
    <br>
    <div class="social-icons">
    {social_links}
    </div>
    <!-- RESUME-ENTRY -->
    </div>
    </section>
    <hr class="m-0" />
    <!-- GitHub Stats-->
    <section class="resume-section" id="gitHubstats">
    <div class="resume-section-content">
    <h2 class="mb-5">GitHub Stats</h2>
    <!-- GITHUBSTATS-ENTRY -->
    </div>
    </section>
    <hr class="m-0" />
    <!-- Projects-->
    <section class="resume-section" id="projects">
    <div class="resume-section-content">
    <h2 class="mb-5">My Projects 👇</h2>
    {project_repos}
    </div>
    </section>
    <hr class="m-0" />
    <!-- HACKATHON-ENTRY -->
    <!-- BLOGS-ENTRY -->
    <!-- FOOTER-ENTRY -->
    </div>
    <!-- Bootstrap core JS-->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Third party plugin JS-->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.min.js"></script>

    <!-- Smooth Scrolling JS-->
    <script src="https://kaustubhgupta.github.io/themescss/script.js"></script>
    </body>

    </html>

    '''

    if stats_choice == '1':
        statsImg = f'''<img class="img-fluid" src="https://github-readme-stats.vercel.app/api?username={user_data['username']}&show_icons=true&theme=radical&count_private=true">'''
        template = template.replace('<!-- GITHUBSTATS-ENTRY -->', statsImg)
        
    elif stats_choice == '2':
        statsImg = f'''<img class="img-fluid" src="https://metrics.lecoq.io/{user_data['username']}?followup=1&isocalendar=1">'''
        template = template.replace('<!-- GITHUBSTATS-ENTRY -->', statsImg)

    if blogs:
        template = addBlogsEntryL2(template)

    try: 
        result = strtobool(resume_link) 
    except:
        result = resume_link

    if type(result) is not int:
        template = addResumeEntryL2(template, resume_link)

    if footer is True:
        template = footer(template)

    if hackathon_repos is not None:
        retunFile = addHackathonEntryL2(hackathon_repos, user_data, template)
        return retunFile
    else:
        return template