## Which Tools You Used and What For

During the planning stage I consulted with an LLM (ChatGPT 6-Luna) on what Python libraries existed for building TUIs. I asked for a list of libraries and a table listing potential use cases, pros, cons, and links. Among the many suggestions were the two I picked `questionary` and `rich`.

I also consulted with the same LLM for advice on how I should organise the project structure, here I just asked what a theoretical structure should look like. I additionally asked for example applications of things developed using `uv` to see what other people are doing.

## How You Verified the Suggestions

To verify the suggested libraries I checked the associated GitHub pages for each. I looked at the dates of the last release (to make sure the project is active), the total stars (to make sure the project is reasonably active) and the README (to see how feasible each library would be for my project).

The rationale for checking the GitHub for each prospective library is to make sure that the project is both legit and active. I have asked LLMs for advice on what libraries do x job before, and some have suggestions have been nonsensical (i.e. 10+ years since last commit, does something unrelated to the problem I want solved). I have also had issues with hallucinated libraries before (libraries that don't exist), doing these checks prevents this from happening as well.

Similarly with the project structure, I looked at what other people were doing. Made note of best practices and applied them to my project.

## Additional Info

One of the third party libraries ([`tmdbsimple`](https://github.com/celiao/tmdbsimple)) contains commits from Claude.
