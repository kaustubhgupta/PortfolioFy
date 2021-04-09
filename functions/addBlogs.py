def addBlogsEntryL1(index_file):
    blogTemplate = '''
    <h1 style="color:#d45131"> My Latest Blogs✍️</h1>
    <div align='left' class="div-blog">
    <!-- BLOG-POST-LIST:START --><!-- BLOG-POST-LIST:END -->
    </div>
    '''
    temp_file = index_file.replace('<!-- BLOG-ENTRY -->', blogTemplate)
    return temp_file

def addBlogsEntryL2(index_file):
    nav_template = '''
    <li class="nav-item"><a class="nav-link js-scroll-trigger" href="#blogs">Latest Blogs</a></li>
    '''
    temp_file = index_file.replace('<!-- BLOGS-NAV-ENTRY -->', nav_template)
    blog_template = '''
        <section class="resume-section" id="blogs">
            <div class="resume-section-content">
                <h2 class="mb-5">Blogs</h2>
                <!-- BLOG-POST-LIST:START --><!-- BLOG-POST-LIST:END -->
            </div>
        </section>
        <hr class="m-0" />
    '''
    final_file = temp_file.replace('<!-- BLOGS-ENTRY -->', blog_template)
    return final_file
