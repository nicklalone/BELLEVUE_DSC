# DSC510 - Week 9
## Getting started with Markdown
This week, we're going to talk about writing a program to make a report. Once we get our code up to snuff, we're going to upload it to our repository AND then we will work on editing it a bit.

1. Generate a report using your previous work.
2. Generate a report in markdown that you can send elsewhere. 

The nice part about generating a report in Markdown is that you can do a number of things with it. For example, you can export that to HTML, PDF, or any sort of file you need. It is a tremendously useful skill to have some exposure to. 

While much of your coding this week will be minimal, it will still be tough. 

---
The sort of learning path we'll expect from you this week is "mostly" straight forward.

1. You will learn about Markdown.
2. Then you will read about generating Markdown with Python.
3. Then you will apply those things to a starter script.

### What is Markdown?

[First Python Notebook: Hello Markdown](http://www.firstpythonnotebook.org/markdown/)
[ Full Stack Python on Markdown](https://www.fullstackpython.com/markdown.html)

In the end, Markdown is a language that can be extended and used for other languages. For example, I use these all the time: 

[Convert Markdown to HTML](https://markdowntohtml.com/)
[Tables Generator](https://www.tablesgenerator.com/)
[Pandoc](https://pandoc.org/)

The whole point of this is that you can use Python to generate markdown files and through markdown, you have access to any readable format out there. It's an incredibly useful skill to have. Additionally, you will notice that all of the readme files and various documentation files on GITHUB use markdown. This will help you when creating your portfolio. 

### How can I do stuff with Markdown using Python?.

Well, quite simply you can trick it by manually adding this stuff to your print statements that looks like markdown. For example, after the midterm, you would have been asked to continue creating the class object *avenger*. Through that class, you'd have written print statements that provide the characters needed for Header levels, new lines, and bulleted lists. 

There is an example script in the folder called, `LALONE_MSDS510`. Let's talk about that!

### The Starter Script.

Before I get started, I wanted to say that the chapters 26-29 were required reading for this week. While they are no longer required reading, they will be useful for you to look through to make this thing work!

There are a few files and folders inside of the repository `LALONE_MSDS510`. It is the *avenger* class and various utilities that we would have created ourselves had we stuck with the breakneck speed of the course. In all honesty, creating this script could take an entire semester itself. Instead of building it all, we will encounter a likely scenario in the coding world. Someone created it before you, didn't document it well, and you've inherited it as it is suddenly broken. From what we can see, it is missing some of the end of the Markdown Statement. 

From that perspective, we could also say that I have given you a scaffold upon which you will build more content. Your job is to use all your resources to get it finished. 

In addition to the script for the `avengers` class, there is also a file in MSDS_LALONE called, "Make Report." It is also missing an items. Namely, how do you connect the avenger class to the file? do I just say something like, `from msds510.avengers import something?` What do I import? Would that even work? 

Experiment and find out?

## What `specifically` is the assignment this week?

1. Download the directory `LALONE_MSDS510` and copy the new scripts into your working folder.
1. Evaluate and finish the avenger class so that it can generate a markdown report. Be sure to check the example report.
1. Correct the `make_report.py` file so that it will import the Avenger class and work correctly from the command line.
1. Upload your working code to the Github Repository into your folder by this Thursday.
1. Help other students out by commenting on their code or correcting their code.
