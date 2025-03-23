# marketing-MAS-multi-agent-system
this project will contain a MAS marketing agency that makes posts for the relevan social medias and emails


# Project Overview
Welcome to this innovative project that aims to develop a unique, AI-driven marketing system. The project's foundation lies in a comprehensive **Marketing Research Document** (the name might need adjustment to reflect company-specific details). This document will include:

- **Target Demographics**  
- **Company Beliefs** (e.g., eco-friendly production)  
- **Key Features of the Company**  
- **Company Slogan**  
- **Social Media Strategy Overview:** What type of content the company aims to post — a guideline for the multi-agent system  
- **Key Metrics for Success:** What constitutes a successful post based on engagement and reach  

---

## Requirements
To run this project, you will need:

- An **OpenAI API Key**: Obtain it from [OpenAI Platform](https://platform.openai.com/).  

---

## Project Functionality
This system processes the Marketing Research Document, storing and utilizing it for **RAG** (Retrieval-Augmented Generation). The information is used to guide AI agents in creating and managing social media posts effectively.  

### Workflow Overview
1. **Data Storage and Retrieval:**  
   The marketing research document is saved in the project's database, providing context for the AI agents.  

2. **AI Agents:**  
   The system has a series of specialized agents that collaborate to create optimized social media content:  
   - **Research Agent:** Analyzes the document to identify valuable marketing information.  
   - **Trend Analysis Agent:** Simultaneously researches trending content within the target demographic.  
   - **Supervisor Agents:** Evaluate and monitor posts for compliance with company beliefs. If necessary, they request revisions from the Editor Agent.  

### The 4 Key Agents  
#### 1. Writer Agent  
- Uses marketing strategies to craft tailored social media posts for specific platforms.  
- Submits drafts to the Editor Agent for approval.  
- Adjusts the content if the Editor requests revisions.  

#### 2. Editor Agent  
- Reviews posts for accuracy, adherence to company beliefs, and platform-specific standards.  
- Approves posts or sends them back to the Writer Agent for modifications.  
- Forwards approved posts to the Supervisor Agents for final checks.  

#### 3. Photo Prompt Engineer Agent  
- Creates AI prompts for **DALL-E** to generate images, if applicable.  
- Saves images in a designated folder alongside the corresponding post text.  

#### 4. Post Agent  
- Publishes the finalized post to the target social media platform.  
- Ensures correct placement of text, images, and tags.  
- Stores the URL of the published post for future analysis.  

---

## System Behavior
- **First Run:**  
  Follows the standard process outlined above.  

- **Subsequent Runs:**  
  Additionally, the system:  
  - Scrapes past posts to analyze user interaction.  
  - Learns from audience preferences to optimize future content.  
  - Prevents repetitive content and adapts to the evolving interests of the target demographic.  





