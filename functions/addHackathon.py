def addHackathonEntryL1(hackathons, user_data, intermediate):
    template = f'''
    <h1 style="color:#d45131"> Hackathons I participated👇</h1>
    <text class="text-info">(These repositories are tagged as project. *Updated: {user_data['latest_updated']})</text>
    <br>
    {hackathons}
    '''
    returnedFile = intermediate.replace('<!-- HACKATHON-ENTRY -->', template)
    return returnedFile

def addHackathonEntryL2(hackathons, user_data, intermediate):
    nav_template = '''
    <li class="nav-item"><a class="nav-link js-scroll-trigger" href="#hackathons">Hackathons</a></li>
    '''
    temp_file = intermediate.replace('<!-- HACKATHON-NAV-ENTRY -->', nav_template)
    hackathon_template = f'''
        <section class="resume-section" id="hackathons">
            <div class="resume-section-content">
                <h2 class="mb-5">Hackathons</h2>
                {hackathons}
            </div>
        </section>
         <hr class="m-0" />
    '''
    returned_file = temp_file.replace('<!-- HACKATHON-ENTRY -->', hackathon_template)
    return returned_file