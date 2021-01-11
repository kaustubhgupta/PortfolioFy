from functions.addBlogs import addBlogsEntryL2
from functions.addHackathon import addHackathonEntryL2


def genHTMLLevel2(user_data, project_repos, hackathon_repos, blogs, stats_choice):

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
    <a class="social-icon" href="https://github.com/{user_data['username']}"><svg class="svg-inline--fa fa-github fa-w-16" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="github" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 496 512" data-fa-i2svg=""><path fill="currentColor" d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"></path></svg></a>
    </div>
    <a href="https://drive.google.com/file/d/13aERPhQiXCqY04NusEhWW2sTSy-A3g-c/view?usp=sharing" target="_blank"><h4 style='color:#d45131; margin:20px 0;'>View Resume</h4></a>
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

    if hackathon_repos is not None:
        retunFile = addHackathonEntryL2(hackathon_repos, user_data, template)
        return retunFile
    else:
        return template
