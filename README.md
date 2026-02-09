# Inter Prep
A preparation Assistant
This works using the groq api keys and uses the llama 3.3 7b versatile model
It uses the yutube api to generate the relevant youtube video results
Used some plotting stuff to track the progress of the user
Could use a database to Track the progress on the long run
It works perfectly well for a single sitting


A Streamlit app for generating study checklists and quizzes with YouTube video recommendations.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/NGHTFury05/Inter-Prep.git
   cd Inter-Prep

2.Get a Groq API key from Groq.
  Get a YouTube API key from Google Cloud Console.

	GROQ_API_KEY=your_groq_api_key
	YOUTUBE_API_KEY=your_youtube_api_key

3.Create a .env file in the root directory with your API keys:

GROQ_API_KEY=your_groq_api_key
YOUTUBE_API_KEY=your_youtube_api_key

4.pip install -r requirements.txt

5. Finally Run the App with 
  streamlit run 2.py

#Features
 Generate study checklists
 Take quizzes
 View YouTube video recommendations