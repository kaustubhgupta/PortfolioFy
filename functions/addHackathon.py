def addHackathonEntry(hackathons, user_data, intermediate):
    template = f'''
    <h1 style="color:#d45131"> Hackathons I participated👇</h1>
    <text class="text-info">(These repositories are tagged as project. *Updated: {user_data['latest_updated']})</text>
    <br>
    {hackathons}
    '''
    returnedFile = intermediate.replace('<!-- HACKATHON-ENTRY -->', template)
    return returnedFile