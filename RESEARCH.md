## What You Needed to Learn and Why

Before I started the development I created a plan. This plan included a step by step breakdown of what I wanted this app to do and libraries I would have to use. When choosing what language to use I chose Python, as I have past with it. The goal with creating the plan is that it makes the app easier to develop as I have a checklist of things to do.

This tool uses 3 libraries I haven't used before (`tmdbsimple`, `questionary`, and `rich`), I used the documentation for each library for learning how to use them.

The TMDB API was also something I had to learn, I eventually used `tmdbsimple` deal with it. To learn what parts of the output I needed I printed out the entire response and made note of any useful keys.

I decided to learn a new tool to help with the documentation. I came across [`vhs`](https://github.com/charmbracelet/vhs) recently, and decided it would be useful for creating a demo video. Videos are created by writing commands into a `.tape` file, easily creating a demo video. Without this tool I would have had to use a screen recorder such as OBS.

## Where You Looked and How You Assessed the Information

During the planning stage I consulted with LLMs to help decide what libraries to use.

To learn the tools I checked their associated documentation. This was useful as they more often than not contained code snippets and a breakdown of what each library method does. This was most useful with `questionary` and `rich` as both tools were new to me.

Additional useful information came from my code editor's parameter hints, `ruff` (python linter) and `basedpylance` (type checker). These tools highlighted potential issues and give informative descriptors of what various functions, methods, and libraries do. One example of this being useful, is that optional arguments for library methods. When I was creating the input forms using `questionary`, I noticed that there was an option for validation, I used this to make sure it was impossible for an invalid year to be entered.

## Problems or Approaches That Didn't Work

I was originally planning on using `requests` to deal with the TMDB API, but after consulting the TMDB documentation they suggest numerous wrappers/libraries, I picked the most popular one available for Python which was `tmdbsimple`.

I did remove `requests` as a hard dependency at one point, but added it back to help catch errors associated with invalid API keys.

## What You Learned

That planning is the most important part of every project.

Having an adequate plan, gives a structured workflow for developing and potentially allows you to see issues before they emerge. The goal with this project was to build something within 3 hours, although I did go slightly over this time allowance due to experimenting with tools in both the planning stage and development stage. This is why the 'Future Improvements' section of the README is quite long (and includes bugs), there is a lot I wanted to do within the allocated time that I couldn't.

I made the assumption that I could list out a bunch of requirements, draw up a sequence diagram and then assume that the development would take a certain amount of time (3 hours). I underestimated the scope of the problem and how long it takes to fully learn new libraries and tools. To remedy this in the future better planning that incoporates timeframes would be useful.
