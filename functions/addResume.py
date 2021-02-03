def addResumeEntryL1(index_file, resume_link):
    resumeTemplate = f'''
    <a href="{resume_link}" target="_blank"><h2 style='color:#d45131'>👉View Resume</h2></a>
    '''
    temp_file = index_file.replace('<!-- RESUME-ENTRY -->', resumeTemplate)
    return temp_file

def addResumeEntryL2(index_file, resume_link):
    resumeTemplate = f'''
    <a href="{resume_link}" target="_blank"><h4 style='color:#d45131; margin:20px 0;'>View Resume</h4></a>
    '''
    temp_file = index_file.replace('<!-- RESUME-ENTRY -->', resumeTemplate)
    return temp_file
    