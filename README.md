# 🚀 Marketing MAS Multi-Agent System

Welcome to the **Marketing MAS Multi-Agent System** project! This innovative platform is designed to power a fully AI-driven marketing agency that creates and manages social media posts and emails using a team of specialized agents.

---

## 📑 Project Overview

Our system leverages a comprehensive **Marketing Research Document** (name may be adjusted for company-specific needs) that includes:
- **Target Demographics** 👥  
- **Company Beliefs** 🌱 (e.g., eco-friendly production)  
- **Key Features of the Company** ✨  
- **Company Slogan** 🗣️  
- **Social Media Strategy Overview** 📱: Guidelines for the type of content the company aims to post  
- **Key Metrics for Success** 📊: Engagement and reach targets that define a successful post

---

## 🛠️ Requirements

- **Python**: Version >=3.10 and <=3.13  
- **Poetry**: For dependency management and package handling  
- **OpenAI API Key**: Obtain from [OpenAI Platform](https://platform.openai.com/) 🔑

---

## 🔧 Installation

1. **Install Poetry**  
   If you haven't already, install Poetry:
   ```
   pip install poetry
   ```

2. **Clone the Repository and Install Dependencies**  
   Navigate to your project directory and install the dependencies:

   ```
   poetry lock
   poetry install
   ```

3. **Customizing**  
   - Create a `.env` file in the root directory and add your `OPENAI_API_KEY`:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

4. **Adding Company Data**  
   Place your company data file (for now, using the provided fictional example) in:
   ```
   src/research_crew/Data/marketing information.txt
   ```
   This file serves as a template and should be replaced with your real marketing research document.

---

## 🚀 Running the Project

To start your crew of AI agents and begin task execution, run the following command from the root folder of your project:

```
poetry run research_crew
```
*(Note: "research_crew" is a temporary name; feel free to suggest an alternative once you decide on the final project name.)*

---

## ✅ Tasks

- [x] Create project  
- [x] Add Post Agent for Instagram  
- [ ] Add Post Agent for Facebook  
- [ ] Add Post Agent for X.com  
- [ ] Add Post Agent for Threads  
- [ ] Add Agent for Email Marketing  
- [ ] Add Agent for Email Newsletter  

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## 📬 Contact Information

For any questions or suggestions, please contact me at:  
**Email:** [stilianmatev@gmail.com](mailto:stilianmatev@gmail.com)
