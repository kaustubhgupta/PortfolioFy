

class Adder:
    '''
    This class of functions contains all the additional functions required to add the website components.
    '''

    def __init__(self):
        pass

    def addBlogsL1(self, index_file: str) -> str:
        '''
        Function to add blogs section and meta text (comment) needed for blogpost workflow in level 1 theme.
        '''

        L1_template = '''  
        <h1 style="color:#d45131"> My Latest Blogs✍️</h1>
        <div align='left' class="div-blog">
        <!-- BLOG-POST-LIST:START --><!-- BLOG-POST-LIST:END -->
        </div>
        '''
        temp_file = index_file.replace('<!-- BLOG-ENTRY -->', L1_template)
        return temp_file

    def addBlogsL2(self, index_file: str) -> str:
        '''
        Function to add blogs section and meta text (comment) needed for blogpost workflow in level 2 theme. 
        For theme 2, "Blogs" section needed to be added both in Menu (Navigation) bar and main section  
        '''

        nav_template = '''
        <li class="nav-item"><a class="nav-link js-scroll-trigger" href="#blogs">Latest Blogs</a></li>
        '''

        temp_file = index_file.replace(
            '<!-- BLOGS-NAV-ENTRY -->', nav_template)

        L2_template = '''
            <section class="resume-section" id="blogs">
                <div class="resume-section-content">
                    <h2 class="mb-5">Blogs</h2>
                    <!-- BLOG-POST-LIST:START --><!-- BLOG-POST-LIST:END -->
                </div>
            </section>
            <hr class="m-0" />
        '''
        final_file = temp_file.replace('<!-- BLOGS-ENTRY -->', L2_template)
        return final_file

    def addFooter(self, index_file: str) -> str:
        '''
        Function to add creator credits at the end of the webpage generated. 
        '''

        footer_template = '''<p class="text-info">Generated by <a href="https://github.com/kaustubhgupta">Kaustubh Gupta</a></p>'''

        replacement = index_file.replace(
            "<!-- FOOTER-ENTRY -->", footer_template)
        return replacement

    def addHackathonL1(self, hackathons: str, lastUpdated: str, intermediate: str) -> str:
        '''
        Function to add hackathons data in level 1 theme
        '''

        hackathonTemplate = f'''
        <h1 style="color:#d45131"> Hackathons I participated👇</h1>
        <text class="text-info">*Updated: {lastUpdated}</text>
        <br>
        {hackathons}
        '''
        indexWithHackathon = intermediate.replace(
            '<!-- HACKATHON-ENTRY -->', hackathonTemplate)
        return indexWithHackathon

    def addHackathonL2(self, hackathons: str, lastUpdated: str, intermediate: str) -> str:
        '''
        Function to add hackathons data to level 2 theme. Here, the navigation menu also needs to be updated for hackathon section.
        '''

        nav_template = '''
        <li class="nav-item"><a class="nav-link js-scroll-trigger" href="#hackathons">Hackathons</a></li>
        '''
        indexWithNav = intermediate.replace(
            '<!-- HACKATHON-NAV-ENTRY -->', nav_template)

        hackathonTemplate = f'''
            <section class="resume-section" id="hackathons">
                <div class="resume-section-content">
                    <h2 class="mb-5">Hackathons</h2>
                    <text class="text-info">*Updated: {lastUpdated}</text>
                    <br>
                    {hackathons}
                </div>
            </section>
            <hr class="m-0" />
        '''
        indexWithHackathon = indexWithNav.replace(
            '<!-- HACKATHON-ENTRY -->', hackathonTemplate)

        return indexWithHackathon

    def addResumeL1(self, index_file: str, resume_link: str) -> str:
        '''
        Function to add "View Resume" hyperlink in level 1 theme
        '''

        resumeTemplate = f'''
        <a href="{resume_link}" target="_blank"><h2 style='color:#d45131'>👉View Resume</h2></a>
        '''

        indexWithResume = index_file.replace(
            '<!-- RESUME-ENTRY -->', resumeTemplate)
        return indexWithResume

    def addResumeL2(self, index_file: str, resume_link: str) -> str:
        '''
        Function to add "View Resume" hyperlink in level 1 theme
        '''

        resumeTemplate = f'''
        <a href="{resume_link}" target="_blank"><h4 style='color:#d45131; margin:20px 0;'>View Resume</h4></a>
        '''

        indexWithResume = index_file.replace(
            '<!-- RESUME-ENTRY -->', resumeTemplate)
        return indexWithResume
