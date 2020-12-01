def addBlogsEntry(index_file):
    blogTemplate = '''
    <h1 style="color:#d45131"> My Latest Blogs✍️</h1>
    <div align='left' class="div-blog">
    <!-- BLOG-POST-LIST:START -->
    <!-- BLOG-POST-LIST:END -->
    </div>
    '''
    index_file = index_file.replace('<!-- BLOG-ENTRY -->', blogTemplate)
    return index_file