# marketing-MAS-multi-agent-system
this project will contain a MAS marketing agency that makes posts for the relevan social medias and emails

# overview of the project
Hi, this project will have a special marketing system
it will need a marketing research document for the company( the name of the document may need to change, because it needs to have info about the company too),
that it will contain the target demograpic, 
beliefs(eco production for example), 
Key Features of the company,
slogan for the company would be great, 
because how the social media works
and an overview of what kind of posts 
the company wants to post on the social media 
- as a guideline for the multi agent system
and key metrics for success - what do you consider a success for the posts that the system makes?

# requirements
to run this project you would need to have an OpenAI API key
you can get it from https://platform.openai.com/
you would need to enter at least 5$, or equivalent in your currency,
if you don't have an API key already.

# what will the project do?
the project will recieve the marketing research document and it will and will store it in its database
It will use it for RAG - Retrieval-augmented generation
it will store it and contain the necessary information and it will give it to the models as needed

afterwards the first model of the system will recieve the information and will see what can be used for markeding posts
there would be a second agent, that will simutaniosly research the social media for what kind of posts are trending with the target demographic.
after they are done, the information, that was gathered from these two agents will be given to the supervisor agents for different platforms.
they will supervise and quality check posts for if they conform to the company's beliefs before they are posted.
if there are any discrepancies, it would return the post to the editor agent to fix it with instructions on what needs fixing 
the supervisor will have 4 agents underneat him
1. Writer agent
2. Editor agent   
3. Photo prompt engineer agent
4. post agent

1) Writer agent
  this agent will recieve the current marketing strategies and information for posts for his coresponding platform that he needs to write post in.
He will write the post and after we writes it and is happy with the result it will send it to the editor to check and approve it.
if the editor doesn't like the post, it will retun it to the writer to fix it

2) Editor agent
This agent recieves the post made from the writer agent and checks if it is correct, \
if it corresponds to the company beliefs and other things to make sure the post will be good for the coresponding social media
after it is done it sends it to the supervisor for him to do a final check and return if the post needs to be changed.

3) Photo prompt engineer agent
 This agent will recieve the marketing strategy, information about the company and the finished post text.
It recieves the information and makes a prompt for DALL-E to generate a picture for the post, if the platform that it caters to can have a picture.
it saves the picture in a folder with the post text and is done.

4) Post agent
   This agent has a task to post the post in the social media correctly -
   to put the image if platform can accept images,
   to put the tags if the platform can have tags,
   to put the text correctly
   and to finaly post it
   it will save the url of the posted post for later analys of user interaction
 

if this is the first time the program is run, this is how it will operate
if this is any other time the program is run, it will also do one more step in the beggining
- it will scrape the previosly made posts to see how the users interacted with the post for future post optimization
that way it won't make the same post twice and will know what the target demographic likes and dislikes and change the posts in a way to make them likeable





