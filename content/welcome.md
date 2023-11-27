title: The first post of the blog
date: 2023-11-27T11:43:17-06:00

Welcome!

My portfolio is finally up and running on GitHub Pages after spending quite some time thoroughly understanding the workflow required to create a static website using Pelican as well as thinking about what to write about.

This site uses simple CSS so content is legible on both desktop and mobile devices. I will be primarily using this website to showcase my projects.

The site allows for code syntax highlighting. See below for an example.

    ::python
    import os

    filename = 'very_large_file.txt'
    def read_and_print(filename):
        """
        Open the file in read mode and lazily read in and print each line using the file object iterator.
        This is to avoid loading all of the file into memory at once in the case of very large files.
        """
        filepath = os.path.join(os.path.dirname(__file__), filename)
        with open(filepath, 'r') as myfile: 
            for line in myfile: 
                print(line)

